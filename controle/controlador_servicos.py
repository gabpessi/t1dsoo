from limite.tela_servico import TelaServico
from entidade.servico import Servico
from DAOs.servico_dao import ServicoDAO
from exceptions.lista_vazia_exception import ListaVaziaException
from exceptions.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exceptions.objeto_repetido_exception import ObjetoRepetidoException


class ControladorServicos():
    def __init__(self, controlador_sistema):
        self.__servico_DAO = ServicoDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_servico = TelaServico()

    def pega_servico_por_codigo(self, codigo):
        for servico in self.__servico_DAO.get_all():            
            if servico.codigo == codigo:
                return servico
        return None   
    

    def incluir_servico(self):
        dados_servico = self.__tela_servico.pega_dados_servico()
        if not dados_servico:
            return
        codigo = dados_servico["codigo"]     
        servico = self.pega_servico_por_codigo(codigo)
        try:
            if servico == None:
                servico = Servico(dados_servico["nome"], dados_servico["preco"], dados_servico["codigo"])
                self.__servico_DAO.add(servico)
                self.__tela_servico.mostra_mensagem("Servico cadastrado com sucesso")
            else:
                raise ObjetoRepetidoException("Código de servico", codigo)
            
        except ObjetoRepetidoException as e: 
            self.__tela_servico.mostra_mensagem(e) 

    def alterar_servico(self):
        try:
            if not self.__servico_DAO.get_all():
                raise ListaVaziaException("serviços")
            
            self.lista_servico()

            while True:
                try:
                    codigo_servico = self.__tela_servico.seleciona_servico()
                    if codigo_servico is None:
                        return
                    
                    servico = self.pega_servico_por_codigo(codigo_servico)
                    if servico is None:
                        raise ObjetoNaoEncontradoException("Serviço")
                    break
                
                except ObjetoNaoEncontradoException as e:
                    self.__tela_servico.mostra_mensagem(f"Erro: {str(e)} Por favor, tente novamente.")
                except Exception as e:
                    self.__tela_servico.mostra_mensagem(f"Erro: {str(e)} Por favor, corrija os dados.")

            novos_dados_servico = self.__tela_servico.pega_dados_servico()
            servico.nome = novos_dados_servico["nome"]
            servico.preco = novos_dados_servico["preco"]
            self.__servico_DAO.update(servico)
            self.lista_servico()

        except ListaVaziaException as e:
            self.__tela_servico.mostra_mensagem(e)



    def lista_servico(self):
        dados_servicos = []
        try:   
            if not self.__servico_DAO.get_all():
                raise ListaVaziaException("servicos")   
            for servico in self.__servico_DAO.get_all():
                dados_servicos.append({"nome": servico.nome, "preco": servico.preco, "codigo": servico.codigo})
            self.__tela_servico.mostra_servico(dados_servicos)
        except ListaVaziaException as e:
            self.__tela_servico.mostra_mensagem(e)

    def excluir_servico(self):
        try:
            if not self.__servico_DAO.get_all():
                raise ListaVaziaException("servicos")
            self.lista_servico()
            codigo_servico = self.__tela_servico.seleciona_servico()
            servico = self.pega_servico_por_codigo(codigo_servico)

            if servico is not None:                
                self.__servico_DAO.remove(servico.codigo)
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

    