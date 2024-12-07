from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente
from DAOs.cliente_dao import ClienteDAO
from exceptions.lista_vazia_exception import ListaVaziaException
from exceptions.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exceptions.objeto_repetido_exception import ObjetoRepetidoException

class ControladorClientes():
    def __init__(self, controlador_sistema):
        self.__cliente_DAO = ClienteDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()

    def pega_cliente_por_cpf(self, cpf: str):
        for cliente in self.__cliente_DAO.get_all():
            if(cliente.cpf == cpf):
                return cliente
        return None    
    
    def seleciona_cliente(self):
        return self.__tela_cliente.seleciona_cliente()    

    def incluir_cliente(self):        
        dados_cliente = self.__tela_cliente.pega_dados_cliente()     
        if not dados_cliente:
            return  

        cpf = dados_cliente["cpf"]
        cliente = self.pega_cliente_por_cpf(cpf)
        veterinario = self.__controlador_sistema.controlador_veterinarios.pega_veterinario_por_cpf(cpf)

        try:            
            if cliente is None and veterinario is None:
                cliente = Cliente(dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["email"], cpf)               
                self.__cliente_DAO.add(cliente)
                self.__tela_cliente.mostra_mensagem("Cliente cadastrado com sucesso")
            else:               
                raise ObjetoRepetidoException("CPF", cpf)

        except ObjetoRepetidoException as e:            
            self.__tela_cliente.mostra_mensagem(e)

    def alterar_cliente(self):
        try:
            if not self.__cliente_DAO.get_all():
                raise ListaVaziaException("clientes")            
            self.lista_cliente()

            while True:
                try:
                    cpf_cliente = self.__tela_cliente.seleciona_cliente()
                    if cpf_cliente is None:
                        return
                    
                    cliente = self.pega_cliente_por_cpf(cpf_cliente)
                    if cliente is None:
                        raise ObjetoNaoEncontradoException("Cliente")                   
                    break
                
                except ObjetoNaoEncontradoException as e:
                    self.__tela_cliente.mostra_mensagem(f"Erro: {str(e)}. Por favor, tente novamente.")
                except Exception as e:
                    self.__tela_cliente.mostra_mensagem(f"Erro: {str(e)}. Por favor, corrija os dados.")

            
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            cliente.nome = novos_dados_cliente["nome"]
            cliente.telefone = novos_dados_cliente["telefone"]
            cliente.email = novos_dados_cliente["email"]            
            self.__cliente_DAO.update(cliente)
            self.lista_cliente()

        except ListaVaziaException as e:
            self.__tela_cliente.mostra_mensagem(e)

    def lista_cliente(self):    
        dados_clientes = [] 
        try:   
            if not self.__cliente_DAO.get_all():
                raise ListaVaziaException("clientes")             
            for cliente in self.__cliente_DAO.get_all():     
                dados_clientes.append({"nome": cliente.nome, "telefone": cliente.telefone, "email": cliente.email, "cpf": cliente.cpf, "animais": cliente.animais})                 
            self.__tela_cliente.mostra_cliente(dados_clientes)

        except ListaVaziaException as e:
            self.__tela_cliente.mostra_mensagem(e)
                    
    def excluir_cliente(self):         
        try:
            if not self.__cliente_DAO.get_all():
                raise ListaVaziaException("clientes") 
            self.lista_cliente()
            cpf_cliente = self.__tela_cliente.seleciona_cliente()
            cliente = self.pega_cliente_por_cpf(cpf_cliente)
        
            if cliente is not None:                
                self.__cliente_DAO.remove(cliente.cpf)
                self.lista_cliente()
            else:
                raise ObjetoNaoEncontradoException("Cliente")        
        
        except ObjetoNaoEncontradoException as e:
            self.__tela_cliente.mostra_mensagem(e)
        except ListaVaziaException as e:
            self.__tela_cliente.mostra_mensagem(e)

    def busca_animal_por_cliente(self, cliente, numero_cadastro):
        for animal in cliente.animais:
            if animal.numero_cadastro == numero_cadastro:
                return animal
        raise ObjetoNaoEncontradoException("Animal")
 
    def incluir_animal(self):
        try:              
            if not self.__cliente_DAO.get_all(): 
                raise ListaVaziaException("clientes") 
            self.lista_cliente()        
            cpf_cliente = self.__tela_cliente.seleciona_cliente() 
            cliente = self.pega_cliente_por_cpf(cpf_cliente)
            if cliente == None:
                raise ObjetoNaoEncontradoException("Cliente")  
                                
            dados_animal = self.__tela_cliente.pega_dados_animal()  

            for c in self.__cliente_DAO.get_all():          
                for animal in c.animais:
                    if animal.numero_cadastro == dados_animal["numero_cadastro"]:
                        raise ObjetoRepetidoException("Animal", dados_animal["numero_cadastro"])
            
            cliente.adicionar_animal(
            dados_animal["nome_animal"],
            dados_animal["especie"],
            dados_animal["raca"],
            dados_animal["idade"],
            dados_animal["numero_cadastro"]
        )            
            self.__tela_cliente.mostra_mensagem("Animal incluído com sucesso.")
            self.__cliente_DAO.update(cliente)  

        except ListaVaziaException as e:
            self.__tela_cliente.mostra_mensagem(e)
        except ObjetoRepetidoException as e:
            self.__tela_cliente.mostra_mensagem(e) 
        except ObjetoNaoEncontradoException as e:
            self.__tela_cliente.mostra_mensagem(e) 
        
    def alterar_animal(self):        
        try:
            if not self.__cliente_DAO.get_all():
                raise ListaVaziaException("clientes")
            
            self.lista_cliente()

            while True:
                try:
                    cpf = self.__tela_cliente.seleciona_cliente()
                    if cpf is None:
                        return                    
                    cliente = self.pega_cliente_por_cpf(cpf)
                    if cliente is None:
                        raise ObjetoNaoEncontradoException("Cliente")
                    
                    if not cliente.animais:
                        raise ListaVaziaException("animais do cliente")                   
                    break

                except ObjetoNaoEncontradoException as e:
                    self.__tela_cliente.mostra_mensagem(f"Erro: {str(e)}. Por favor, tente novamente.")
                except ListaVaziaException as e:
                    self.__tela_cliente.mostra_mensagem(f"Erro: {str(e)}.")
                except Exception as e:
                    self.__tela_cliente.mostra_mensagem(f"Erro inesperado: {str(e)}. Por favor, corrija os dados.")

            self.lista_animal()
            while True:
                try:
                    numero_cadastro = self.__tela_cliente.seleciona_animal()
                    if numero_cadastro is None:
                        return

                    animal = self.busca_animal_por_cliente(cliente, numero_cadastro)
                    if animal is None:
                        raise ObjetoNaoEncontradoException("Animal")                    
                    break

                except ObjetoNaoEncontradoException as e:
                    self.__tela_cliente.mostra_mensagem(f"Erro: {str(e)}. Por favor, tente novamente.")
                except Exception as e:
                    self.__tela_cliente.mostra_mensagem(f"Erro inesperado: {str(e)}. Por favor, corrija os dados.")

            novos_dados_animal = self.__tela_cliente.pega_dados_animal()
            animal.nome_animal = novos_dados_animal["nome_animal"]
            animal.especie = novos_dados_animal["especie"]
            animal.raca = novos_dados_animal["raca"]
            animal.idade = novos_dados_animal["idade"]
            self.__cliente_DAO.update(cliente)
            self.__tela_cliente.mostra_mensagem("Animal alterado com sucesso.")

        except ListaVaziaException as e:
            self.__tela_cliente.mostra_mensagem(e)
        except Exception as e:
            self.__tela_cliente.mostra_mensagem(f"Erro inesperado: {str(e)}")        

    def excluir_animal(self):
        try:
            if not self.__cliente_DAO.get_all():
                raise ListaVaziaException("clientes")
            self.lista_cliente()
            cpf_cliente = self.__tela_cliente.seleciona_cliente()
            cliente = self.pega_cliente_por_cpf(cpf_cliente)

            if cliente is None:
                raise ObjetoNaoEncontradoException("Cliente")
            
            self.lista_animal()
            numero_cadastro = self.__tela_cliente.seleciona_animal()            
            cliente.remover_animal(numero_cadastro)
            self.__cliente_DAO.update(cliente)
            self.__tela_cliente.mostra_mensagem("Animal removido com sucesso.")

        except ListaVaziaException as e:
            self.__tela_cliente.mostra_mensagem(e)
        except ObjetoNaoEncontradoException as e:
            self.__tela_cliente.mostra_mensagem(e)   

    def lista_animal(self):
        try:
            if not self.__cliente_DAO.get_all():
                raise ListaVaziaException("clientes")  

            animais_para_exibir = []

            for cliente in self.__cliente_DAO.get_all():
                if cliente.animais:                    
                    for animal in cliente.animais:
                        animais_para_exibir.append((animal, cliente.cpf))

            if not animais_para_exibir:
                raise ListaVaziaException("animais")

            self.__tela_cliente.mostra_animal(animais_para_exibir)

        except ListaVaziaException as e:
            self.__tela_cliente.mostra_mensagem(e)
        except ObjetoNaoEncontradoException as e:
            self.__tela_cliente.mostra_mensagem(e)



    def pega_animal_por_numero_cadastro(self, numero_cadastro: str):
        for cliente in self.__cliente_DAO.get_all():
            for animal in cliente.animais:
                if animal.numero_cadastro == numero_cadastro:
                    return animal
        return None
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.alterar_cliente, 3: self.lista_cliente, 4: self.excluir_cliente, 5: self.incluir_animal, 6: self.alterar_animal, 7: self.excluir_animal, 8:self.lista_animal, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()   



    