from limite.tela_servico import TelaServico
from entidade.servico import Servico
from exceptions.lista_vazia_exception import ListaVaziaException
from exceptions.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exceptions.objeto_repetido_exception import ObjetoRepetidoException


class ControladorServicos():
    def __init__(self, controlador_sistema):
        self.__servicos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_servico = TelaServico()

    def pega_servico_por_codigo(self, codigo):
        for servico in self.__servicos:            
            if servico.codigo == codigo:
                return servico
        return None   
    

    def incluir_servico(self):
        dados_servico = self.__tela_servico.pega_dados_servico()
        codigo = dados_servico["codigo"]     
        servico = self.pega_servico_por_codigo(codigo)
        try:
            if servico == None:
                servico = Servico(dados_servico["nome"], dados_servico["preco"], dados_servico["codigo"])
                self.__servicos.append(servico)
            else:
                raise ObjetoRepetidoException("Código de servico", codigo)
            
        except ObjetoRepetidoException as e: 
            self.__tela_servico.mostra_mensagem(e) 

    def alterar_servico(self):
        try:
            if not self.__servicos:
                raise ListaVaziaException("servicos") 
            self.lista_servico()
            codigo_servico = self.__tela_servico.seleciona_servico()
            servico = self.pega_servico_por_codigo(codigo_servico)

            if servico is not None:
                novos_dados_servico = self.__tela_servico.pega_dados_servico()
                servico.nome = novos_dados_servico["nome"]
                servico.preco = novos_dados_servico["preco"]
                servico.codigo = novos_dados_servico["codigo"]
                self.lista_servico()
            else:
                raise ObjetoNaoEncontradoException("Servico")

        except ListaVaziaException as e:
            self.__tela_servico.mostra_mensagem(e) 
            return  
        except ObjetoNaoEncontradoException as e:
            self.__tela_servico.mostra_mensagem(e) 


    def lista_servico(self):
        try:   
            if not self.__servicos:
                raise ListaVaziaException("servicos")   
            for servico in self.__servicos:
                self.__tela_servico.mostra_servico({"nome": servico.nome, "preco": servico.preco, "codigo": servico.codigo})

        except ListaVaziaException as e:
            self.__tela_servico.mostra_mensagem(e)

    def excluir_servico(self):
        try:
            if not self.__servicos:
                raise ListaVaziaException("servicos") 
            self.lista_servico()
            codigo_servico = self.__tela_servico.seleciona_servico()
            servico = self.pega_servico_por_codigo(codigo_servico)

            if servico is not None:
                self.__servicos.remove(servico)
                self.lista_servico()
            else:
                raise ObjetoNaoEncontradoException("Servico")
        
        except ObjetoNaoEncontradoException as e:
            self.__tela_servico.mostra_mensagem(e)
        except ListaVaziaException as e:
            self.__tela_servico.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_servico, 2: self.alterar_servico, 3: self.lista_servico, 4: self.excluir_servico, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_servico.tela_opcoes()]()

    