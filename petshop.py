from cliente import Cliente
from produto import Produto
from servico import Servico

class PetShop:
    def __init__(self):
        self.__clientes = []
        self.__servicos = []
        self.__produtos = []

    @property
    def clientes(self):
        return self.__clientes
    
    @clientes.setter
    def clientes(self, clientes: Cliente):
        if not isinstance(clientes, Cliente):
            return
        self.__clientes = clientes

    
    @property
    def servicos(self):
        return self.__servicos
    
    @servicos.setter
    def servicos(self, servicos: Cliente):
        if not isinstance(servicos, Cliente):
            return
        self.__servicos = servicos
    
    @property
    def produtos(self):
        return self.__produtos
    
    @produtos.setter
    def produtos(self, produtos: Cliente):
        if not isinstance(produtos, Cliente):
            return
        self.__produtos = produtos

    def cadastrar_cliente(self, nome: str, email: str, telefone: int):
        cliente = Cliente(nome, email, telefone)
        if cliente in self.__clientes:
            return
        self.__clientes.append(cliente)
        return f"Cliente {nome} cadastrado com sucesso!"
    
    def cadastrar_produto(self, nome: str, preco: int, quantidade_estoque: int):
        produto = Produto(self, nome, preco, quantidade_estoque)
        if produto in self.__produtos:
            return
        self.__produtos.append(produto)

    def listar_produtos(self):
        return [produto.nome for produto in self.__produtos]   
    

    def cadastrar_servicos(self, nome: str, preco: int):
        servico = Servico(self, nome, preco)
        if servico in self.__servicos:
            return
        self.__servicos.append(servico)   

    def listar_servicos(self):
        return[servico.nome for servico in self.__servicos]