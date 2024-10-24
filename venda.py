from cliente import Cliente
from produto import Produto
class Venda:
    def _init_(self, cliente: Cliente, data: str, valor_total: int):
        self.__cliente = cliente        
        self.__data = data
        self.__produtos = []
        self.__valor_total = 0
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        if isinstance(data, str):
            self.__data = data


    @property
    def produtos(self):
        return self.__produtos
    
    @produtos.setter
    def produtos(self, produtos):
        if isinstance(produtos, Produto):
            self.__produtos = produtos


    @property
    def valor_total(self):
        return self.__valor_total
    
    @valor_total.setter
    def valor_total(self, valor_total):
        if isinstance(valor_total, int):
            self.__valor_total = valor_total


    def adicionar_produto(self, produto: Produto, quantidade: int):
        if produto.verificar_disponibilidade(produto):
            self.produtos.append(produto)
            produto.atualizar_estoque(-1)
            self.valor_total += produto.preco
    

    def remover_produto(self, produto: Produto):        
        self.produtos.remove(produto)
        produto.atualizar_estoque(1)
        self.valor_total -= produto.preco

    def calcular_total(self):
        return self.__valor_total
    
    def finalizar_venda(self):       
        mensagem = f'Venda finalizada para {self._cliente.nome}. Valor total: R${self._valor_total:.2f}'        
        self.__produtos = []
        self.__valor_total = 0

        return mensagem