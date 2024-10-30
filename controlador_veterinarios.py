from tela_veterinario import TelaVeterinario
from veterinario import Veterinario
from consulta import Consulta   
from controlador_consultas import ControladorConsultas

class ControladorVeterinarios():
    def __init__(self, controlador_sistema, controlador_consultas):
        self.__veterinarios = []
        self.__controlador_sistema = controlador_sistema
        self.__controlador_consultas = controlador_consultas
        self.__tela_veterinario = TelaVeterinario()

    def pega_veterinario_por_cpf(self, cpf: str):
        for veterinario in self.__veterinarios:
            if(veterinario.cpf == cpf):
                return veterinario
        return None

    def incluir_veterinario(self):
        dados_veterinario = self.__tela_veterinario.pega_dados_veterinario()        
        s = self.pega_veterinario_por_cpf(dados_veterinario["cpf"])
        if s is None:
            veterinario = Veterinario(dados_veterinario["nome"], dados_veterinario["telefone"], dados_veterinario["email"], dados_veterinario["cpf"], dados_veterinario["especialidade"])
            self.__veterinarios.append(veterinario)            
        else:
            self.__tela_veterinario.mostra_mensagem("ATENÇÃO: Veterinário já cadastrado")

    def alterar_veterinario(self):
        self.lista_veterinario()
        cpf_veterinario = self.__tela_veterinario.seleciona_veterinario()
        veterinario = self.pega_veterinario_por_cpf(cpf_veterinario)

        if(veterinario is not None):
            novos_dados_veterinario = self.__tela_veterinario.pega_dados_veterinario()
            veterinario.nome = novos_dados_veterinario["nome"]
            veterinario.telefone = novos_dados_veterinario["telefone"]
            veterinario.email = novos_dados_veterinario["email"]
            veterinario.cpf = novos_dados_veterinario["cpf"]
            veterinario.especialidade = novos_dados_veterinario["especialidade"]
            
            self.lista_veterinario()
        else:
            self.__tela_veterinario.mostra_mensagem("ATENCAO: Veterinário não cadastrado")

# Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_veterinario(self):
        for veterinario in self.__veterinarios:            
            self.__tela_veterinario.mostra_veterinario({"nome": veterinario.nome, "telefone": veterinario.telefone, "email": veterinario.email, "cpf": veterinario.cpf, "especialidade": veterinario.especialidade})

    def excluir_veterinario(self):
        self.lista_veterinario()
        cpf_veterinario = self.__tela_veterinario.seleciona_veterinario()
        veterinario = self.pega_veterinario_por_cpf(cpf_veterinario)

        if(veterinario is not None):
            self.__veterinarios.remove(veterinario)
            self.lista_veterinario()
        else:
            self.__tela_veterinario.mostra_mensagem("ATENCÃO: Veterinário não existente")         
   
    def adicionar_consulta_por_codigo(self):
        self.lista_veterinario()
        cpf_veterinario = self.__tela_veterinario.seleciona_veterinario()  # Novo método para obter o CPF do veterinário
        veterinario = self.pega_veterinario_por_cpf(cpf_veterinario)

        if not veterinario:
            self.__tela_veterinario.mostra_mensagem("Veterinário não encontrado.")
            return

        
        codigo_consulta = self.__tela_veterinario.pega_codigo_consulta()
        consulta = self.__controlador_consultas.pega_consulta_por_codigo(codigo_consulta)

        if consulta:
            veterinario.adicionar_consulta(consulta)
            self.__tela_veterinario.mostra_mensagem("Consulta adicionada à lista do veterinário.")
        else:
            self.__tela_veterinario.mostra_mensagem("Consulta não encontrada.")

    def remover_consulta_por_codigo(self):
        self.lista_veterinario()
        cpf_veterinario = self.__tela_veterinario.seleciona_veterinario()
        veterinario = self.pega_veterinario_por_cpf(cpf_veterinario)

        if not veterinario:
            self.__tela_veterinario.mostra_mensagem("Veterinário não encontrado.")
            return
        
        codigo_consulta = self.__tela_veterinario.pega_codigo_consulta()
        consulta = self.__controlador_consultas.pega_consulta_por_codigo(codigo_consulta)

        if consulta and consulta in veterinario.consultas:
            veterinario.remover_consulta(consulta)
            self.__tela_veterinario.mostra_mensagem("Consulta removida da lista do veterinário.")
        else:
            self.__tela_veterinario.mostra_mensagem("Consulta não encontrada ou não está na lista do veterinário.")

    def listar_consultas_veterinario(self):
        cpf_veterinario = self.__tela_veterinario.seleciona_veterinario()
        veterinario = self.pega_veterinario_por_cpf(cpf_veterinario)

        if not veterinario:
            self.__tela_veterinario.mostra_mensagem("Veterinário não encontrado.")
            return

        if not veterinario.consultas:
            self.__tela_veterinario.mostra_mensagem("Veterinário sem consultas marcadas.")
        else:
            self.__tela_veterinario.mostra_consulta(veterinario.consultas)



    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_veterinario, 2: self.alterar_veterinario, 3: self.lista_veterinario, 4: self.excluir_veterinario, 5: self.adicionar_consulta_por_codigo, 6: self.remover_consulta_por_codigo, 7: self.listar_consultas_veterinario, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_veterinario.tela_opcoes()]()


    