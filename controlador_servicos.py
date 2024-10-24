from tela_servico import TelaServico
from servico import Servico

class ControladorServicos():
    def __init__(self, controlador_sistema):
        self.__servicos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_servico = TelaServico()

    def pega_servico_por_codigo(self, codigo: int):
        for servico in self.__servicos:
            if(servico.codigo == codigo):
                return servico
        return None

    def incluir_servico(self):
        dados_servico = self.__tela_servico.pega_dados_servico()        
        s = self.pega_servico_por_codigo(dados_servico["codigo"])
        if s is None:
            servico = Servico(dados_servico["nome"], dados_servico["preco"], dados_servico["codigo"])
            self.__servicos.append(servico)
        else:
            self.__tela_servico.mostra_mensagem("ATENÇÃO: Serviço já existente")

    def alterar_servico(self):
        self.lista_servico()
        codigo_servico = self.__tela_servico.seleciona_servico()
        servico = self.pega_servico_por_codigo(codigo_servico)

        if(servico is not None):
            novos_dados_servico = self.__tela_servico.pega_dados_servico()
            servico.nome = novos_dados_servico["nome"]
            servico.preco = novos_dados_servico["preco"]
            servico.codigo = novos_dados_servico["codigo"]
            self.lista_servico()
        else:
            self.__tela_servico.mostra_mensagem("ATENCAO: servico não existente")

# Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_servico(self):
        for servico in self.__servicos:
            self.__tela_servico.mostra_servico({"nome": servico.nome, "preco": servico.preco, "codigo": servico.codigo})

    def excluir_servico(self):
        self.lista_servico()
        codigo_servico = self.__tela_servico.seleciona_servico()
        servico = self.pega_servico_por_codigo(codigo_servico)

        if(servico is not None):
            self.__servicos.remove(servico)
            self.lista_servico()
        else:
            self.__tela_servico.mostra_mensagem("ATENCÃO: Servico não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_servico, 2: self.alterar_servico, 3: self.lista_servico, 4: self.excluir_servico, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_servico.tela_opcoes()]()

    