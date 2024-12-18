from limite.tela_veterinario import TelaVeterinario
from entidade.veterinario import Veterinario
from exceptions.lista_vazia_exception import ListaVaziaException
from exceptions.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exceptions.objeto_repetido_exception import ObjetoRepetidoException
from DAOs.veterinario_dao import VeterinarioDAO
class ControladorVeterinarios():
    def __init__(self, controlador_sistema):
        self.__veterinario_DAO = VeterinarioDAO()
        self.__controlador_sistema = controlador_sistema        
        self.__tela_veterinario = TelaVeterinario()

    def pega_veterinario_por_cpf(self, cpf: str):
        for veterinario in self.__veterinario_DAO.get_all():
            if(veterinario.cpf == cpf):
                return veterinario
        return None

    def incluir_veterinario(self):
        dados_veterinario = self.__tela_veterinario.pega_dados_veterinario()
        if not dados_veterinario:
            return
        cpf = dados_veterinario["cpf"]        
        veterinario = self.pega_veterinario_por_cpf(cpf)
        cliente = self.__controlador_sistema.controlador_clientes.pega_cliente_por_cpf(cpf)
        try:
            if veterinario == None and cliente == None:
                veterinario = Veterinario(dados_veterinario["nome"], dados_veterinario["telefone"], dados_veterinario["email"], dados_veterinario["cpf"], dados_veterinario["especialidade"])
                self.__veterinario_DAO.add(veterinario)
                self.__tela_veterinario.mostra_mensagem("Veterinário cadastrado com sucesso")              
            else:
                raise ObjetoRepetidoException("CPF", cpf)
            
        except ObjetoRepetidoException as e: 
            self.__tela_veterinario.mostra_mensagem(e) 

    def alterar_veterinario(self):
        try:
            if not self.__veterinario_DAO.get_all():
                raise ListaVaziaException("veterinários") 
            self.lista_veterinario()
            cpf_veterinario = self.__tela_veterinario.seleciona_veterinario()
            veterinario = self.pega_veterinario_por_cpf(cpf_veterinario)

            if veterinario is not None:
                novos_dados_veterinario = self.__tela_veterinario.pega_dados_veterinario()
                veterinario.nome = novos_dados_veterinario["nome"]
                veterinario.telefone = novos_dados_veterinario["telefone"]
                veterinario.email = novos_dados_veterinario["email"]
                veterinario.especialidade = novos_dados_veterinario["especialidade"] 
                self.__veterinario_DAO.update(veterinario)               
                self.lista_veterinario()
            else:
                raise ObjetoNaoEncontradoException("Veterinário")  
            
        except ListaVaziaException as e:
            self.__tela_veterinario.mostra_mensagem(e) 
            return  
        except ObjetoNaoEncontradoException as e:
            self.__tela_veterinario.mostra_mensagem(e)  


    def lista_veterinario(self):
        dados_veterinarios = []
        try:
            if not self.__veterinario_DAO.get_all():
                raise ListaVaziaException("veterinários")      
            for veterinario in self.__veterinario_DAO.get_all():
                dados_veterinarios.append({"nome": veterinario.nome, "telefone": veterinario.telefone, "email": veterinario.email, "cpf": veterinario.cpf, "especialidade": veterinario.especialidade, "consultas": veterinario.consultas})  
            self.__tela_veterinario.mostra_veterinario(dados_veterinarios)  
        except ListaVaziaException as e:
            self.__tela_veterinario.mostra_mensagem(e)

    def excluir_veterinario(self):
        try:
            if not self.__veterinario_DAO.get_all():
                raise ListaVaziaException("veterinários") 
            self.lista_veterinario()
            cpf_veterinario = self.__tela_veterinario.seleciona_veterinario()
            veterinario = self.pega_veterinario_por_cpf(cpf_veterinario)

            if veterinario is not None:
                self.__veterinario_DAO.remove(veterinario.cpf)
                self.lista_veterinario()
            else:
                raise ObjetoNaoEncontradoException("Veterinário") 
            
        except ListaVaziaException as e:
            self.__tela_veterinario.mostra_mensagem(e) 
            return  
        except ObjetoNaoEncontradoException as e:
            self.__tela_veterinario.mostra_mensagem(e)          
   
    def adicionar_consulta_por_codigo(self):
        try:
            if not self.__veterinario_DAO.get_all():
                raise ListaVaziaException("veterinários")
            
            self.lista_veterinario() 
            cpf = self.__tela_veterinario.seleciona_veterinario() 
            veterinario = self.pega_veterinario_por_cpf(cpf)

            if not veterinario:
                raise ObjetoNaoEncontradoException("Veterinário")            
            codigo_consulta = self.__controlador_sistema.controlador_consultas.seleciona_consulta()
            consulta = self.__controlador_sistema.controlador_consultas.pega_consulta_por_codigo(codigo_consulta)

            if consulta:
                veterinario.adicionar_consulta(consulta)
                self.listar_consultas_veterinario()
                self.__veterinario_DAO.update(veterinario)
                self.__tela_veterinario.mostra_mensagem("Consulta adicionada à lista do veterinário.")
            else:
                raise ObjetoNaoEncontradoException("Código de consulta")
            
        except ListaVaziaException as e:
            self.__tela_veterinario.mostra_mensagem(e) 
            return  
        except ObjetoNaoEncontradoException as e:
            self.__tela_veterinario.mostra_mensagem(e) 

    def remover_consulta_por_codigo(self):
        try:
            if not self.__veterinario_DAO.get_all():
                raise ListaVaziaException("veterinários")            
            self.lista_veterinario()           
            cpf_veterinario = self.__tela_veterinario.seleciona_veterinario()            
            veterinario = self.pega_veterinario_por_cpf(cpf_veterinario)

            if veterinario is None:
                raise ObjetoNaoEncontradoException("Veterinário")            

            self.listar_consultas_veterinario()              
            codigo = self.__controlador_sistema.controlador_consultas.seleciona_consulta()           
            consulta = self.__controlador_sistema.controlador_consultas.pega_consulta_por_codigo(codigo)
       
            if consulta in veterinario.consultas:
                veterinario.remover_consulta(consulta)
                self.__veterinario_DAO.update(veterinario)
                self.listar_consultas_veterinario()
                self.__tela_veterinario.mostra_mensagem("Consulta removida com sucesso.")
            else:
                raise ObjetoNaoEncontradoException("Consulta")

        except ListaVaziaException as e:
            self.__tela_veterinario.mostra_mensagem(e)
        except ObjetoNaoEncontradoException as e:
            self.__tela_veterinario.mostra_mensagem(e)            

    def listar_consultas_veterinario(self):
        try:
            if not self.__veterinario_DAO.get_all():
                raise ListaVaziaException("veterinários")
            encontrou_consultas = False 

            for veterinario in self.__veterinario_DAO.get_all():
                if veterinario.consultas:
                    encontrou_consultas = True
                    
                    self.__tela_veterinario.mostra_consulta(veterinario.consultas, veterinario.cpf)

            if not encontrou_consultas:
                raise ListaVaziaException("consultas dos veterinários")

        except ListaVaziaException as e:
            self.__tela_veterinario.mostra_mensagem(e)
        except ObjetoNaoEncontradoException as e:
            self.__tela_veterinario.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_veterinario, 2: self.alterar_veterinario, 3: self.lista_veterinario, 4: self.excluir_veterinario, 5: self.adicionar_consulta_por_codigo, 6: self.remover_consulta_por_codigo, 7: self.listar_consultas_veterinario, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_veterinario.tela_opcoes()]()


    