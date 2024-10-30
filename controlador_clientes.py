from tela_cliente import TelaCliente
from cliente import Cliente
from consulta import Consulta
from animal import Animal

class ControladorClientes():
    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()

    def pega_cliente_por_cpf(self, cpf: str):
        for cliente in self.__clientes:
            if(cliente.cpf == cpf):
                return cliente
        return None

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()           
        
        s = self.pega_cliente_por_cpf(dados_cliente["cpf"])
        if s is None:
            cliente = Cliente(dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["email"], dados_cliente["cpf"])
            self.__clientes.append(cliente)            
        else:
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: Cliente já cadastrado")

    def alterar_cliente(self):
        self.lista_cliente()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if(cliente is not None):
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            cliente.nome = novos_dados_cliente["nome"]
            cliente.telefone = novos_dados_cliente["telefone"]
            cliente.email = novos_dados_cliente["email"]
            cliente.cpf = novos_dados_cliente["cpf"]
            
            self.lista_cliente()
        else:
            self.__tela_cliente.mostra_mensagem("ATENCAO: Cliente não cadastrado")

# Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_cliente(self):
        for cliente in self.__clientes:            
            self.__tela_cliente.mostra_cliente({"nome": cliente.nome, "telefone": cliente.telefone, "email": cliente.email, "cpf": cliente.cpf, "animais": cliente.animais}) 
                    
    def excluir_cliente(self):
        self.lista_cliente()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
    

        if(cliente is not None):
            self.__clientes.remove(cliente)
            self.lista_cliente()
        else:
            self.__tela_cliente.mostra_mensagem("ATENCÃO: Cliente não existente")    

    def incluir_animal(self):
        cpf_cliente = self.__tela_cliente.seleciona_cliente()  # Seleciona o cliente
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if cliente:
            dados_animal = self.__tela_cliente.pega_dados_animal()
            if dados_animal is None:  # Verifica se o retorno é None
                self.__tela_cliente.mostra_mensagem("Dados do animal não foram fornecidos corretamente.")
                return
            animal = Animal(dados_animal["nome_animal"], dados_animal["especie"], dados_animal["raca"], dados_animal["idade"], dados_animal["numero_cadastro"])
            cliente.animais.append(animal)            
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado.")   

    def alterar_animal(self):
        self.lista_cliente()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if cliente:
            numero_cadastro = self.__tela_cliente.seleciona_animal()  # Seleciona o animal
            for animal in cliente.animais:
                if animal.numero_cadastro == numero_cadastro:
                    novos_dados_animal = self.__tela_cliente.pega_dados_animal()
                    animal.nome_animal = novos_dados_animal["nome_animal"]
                    animal.especie = novos_dados_animal["especie"]
                    animal.raca = novos_dados_animal["raca"]
                    animal.idade = novos_dados_animal["idade"]
                    animal.numero_cadastro = novos_dados_animal["numero_cadastro"]
                    self.__tela_cliente.mostra_mensagem("Animal alterado com sucesso.")
                    return
                
            self.__tela_cliente.mostra_mensagem("Animal não encontrado.")
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado.")


    def excluir_animal(self):
        self.lista_cliente()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        

        if cliente is not None:
            numero_cadastro = self.__tela_cliente.seleciona_animal()  # Seleciona o animal pelo número de cadastro
            for animal in cliente.animais:
                if animal.numero_cadastro == numero_cadastro:
                    cliente.animais.remove(animal)
                    self.__tela_cliente.mostra_mensagem("Animal removido com sucesso.")
                    return
            self.__tela_cliente.mostra_mensagem("Animal não encontrado.")
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado.")  

    def lista_animal(self):
    # Verifica se há clientes cadastrados
        if not self.__clientes:
            self.__tela_cliente.mostra_mensagem("Não há clientes cadastrados.")
            return
        
        # Percorre cada cliente
        for cliente in self.__clientes:
            if cliente.animais:
                print(f"Responsável: {cliente.nome} (CPF: {cliente.cpf})")  # Exibe informações do cliente
                for animal in cliente.animais:
                    # Exibe os dados de cada animal do cliente usando o método da tela
                    self.__tela_cliente.mostra_animal(animal)
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.alterar_cliente, 3: self.lista_cliente, 4: self.excluir_cliente, 5: self.incluir_animal, 6: self.alterar_animal, 7: self.excluir_animal, 8:self.lista_animal, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()   



    