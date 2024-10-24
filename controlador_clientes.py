from tela_cliente import TelaCliente
from cliente import Cliente

class ControladorClientes():
    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_consulta = TelaConsulta()

    def pega_consulta_por_codigo(self, codigo: int):
        for consulta in self.__consultas:
            if(consulta.codigo == codigo):
                return consulta
        return None

    def incluir_consulta(self):
        dados_consulta = self.__tela_consulta.pega_dados_consulta()        
        s = self.pega_consulta_por_codigo(dados_consulta["codigo"])
        if s is None:
            consulta = Consulta(dados_consulta["data"], dados_consulta["horario"], dados_consulta["descricao"], dados_consulta["animal"], dados_consulta["servico"], dados_consulta["codigo"])
            self.__consultas.append(consulta)
        else:
            self.__tela_consulta.mostra_mensagem("ATENÇÃO: Consulta já cadastrada")

    def alterar_consulta(self):
        self.lista_consulta()
        codigo_consulta = self.__tela_consulta.seleciona_consulta()
        consulta = self.pega_consulta_por_codigo(codigo_consulta)

        if(consulta is not None):
            novos_dados_consulta = self.__tela_consulta.pega_dados_consulta()
            consulta.data = novos_dados_consulta["data"]
            consulta.horario = novos_dados_consulta["horario"]
            consulta.descricao = novos_dados_consulta["descricao"]
            consulta.codigo = novos_dados_consulta["codigo"]
            consulta.animal = novos_dados_consulta["animal"]
            consulta.servico = novos_dados_consulta["servico"]
            self.lista_consulta()
        else:
            self.__tela_consulta.mostra_mensagem("ATENCAO: Consulta não cadastrada")

# Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_consulta(self):
        for consulta in self.__consultas:
            self.__tela_consulta.mostra_consulta({"data": consulta.data, "horario": consulta.horario, "descricao": consulta.descricao, "animal": consulta.animal, "servico":consulta.servico, "codigo": consulta.codigo})

    def excluir_consulta(self):
        self.lista_consulta()
        codigo_consulta = self.__tela_consulta.seleciona_consulta()
        consulta = self.pega_consulta_por_codigo(codigo_consulta)

        if(consulta is not None):
            self.__consultas.remove(consulta)
            self.lista_consulta()
        else:
            self.__tela_consulta.mostra_mensagem("ATENCÃO: Consulta não existente")           
   
    def exibir_detalhes(self):
        self.lista_consulta()
        codigo_consulta = self.__tela_consulta.seleciona_consulta()
        consulta = self.pega_consulta_por_codigo(codigo_consulta)

        if consulta is not None:
            self.__tela_consulta.mostra_mensagem(f"Consulta em {consulta.data} no horário {consulta.horario} para {consulta.animal}. Descrição: {consulta.descricao}. Serviço: {consulta.servico}.")
        
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_consulta, 2: self.alterar_consulta, 3: self.lista_consulta, 4: self.excluir_consulta, 5: self.exibir_detalhes, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_consulta.tela_opcoes()]()

    



def adicionar_animal(self, animal: Animal):
        if not isinstance(animal, Animal) or animal in self.__animais:
            return
        self.animais.append(animal)

    def remover_animal(self, animal: Animal):
        self.animais.remove(animal)

    def listar_animais(self):
        return [animal.nome for animal in self.animais]