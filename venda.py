import uuid
from datetime import datetime
from cliente import Cliente
from produto import Produto

class Venda:
    def __init__(self, cliente: Cliente):
        self.__cliente = cliente
        self.__data = datetime.now()
        self.__codigo_venda = str(uuid.uuid4())
        self.__produtos = []
        self.__valor_total = 0.0  # Agora um float

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

    @property
    def produtos(self):
        return self.__produtos

    @property
    def valor_total(self):
        return self.__valor_total
    
    @valor_total.setter
    def valor_total(self, valor_total):
        if isinstance(valor_total, float):
            self.__valor_total = valor_total

    @property
    def codigo_venda(self):
        return self.__codigo_venda  # Corrigido para __codigo_venda

    def adicionar_produto(self, produto: Produto, quantidade: int):
        if isinstance(produto, Produto):
            if quantidade > produto.quantidade_estoque:
                return False  # Indica que não foi possível adicionar o produto
            self.__produtos.append((produto, quantidade))
            produto.atualizar_estoque(-quantidade)
            self.__valor_total += produto.preco * quantidade
            return True  # Indica que o produto foi adicionado com sucesso
        return False  # Produto inválido

    
    def remover_produto(self, produto: Produto):
        for p, q in self.__produtos:
            if p == produto:
                self.__produtos.remove((p, q))
                self.__valor_total -= produto.preco * q
                produto.atualizar_estoque(q)                
                return True  # Indica que a remoção foi bem-sucedida
        return False  # Indica que o produto não foi encontrado na venda

    def listar_produtos(self):
        return [(p.nome, p.quantidade, p.preco) for p in self.__produtos]

    def finalizar_venda(self):
        mensagem = f'Venda finalizada para {self.__cliente.nome}. Valor total: R${self.__valor_total:.2f}'       
        
        return mensagem
