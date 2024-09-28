class Produto:
    def __init__(self, nome: str, preco: int, quantidade_estoque: int):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
       if not isinstance(nome, str):
            return
       self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
       if not isinstance():
            return
       self.__preco = preco    

    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade_estoque):
       if not isinstance(quantidade_estoque, int):
            return
       self.__quantidade_estoque = quantidade_estoque

    
    def verificar_disponibilidade(self: bool):   
        return self.__quantidade_estoque > 0
    
    def atualizar_estoque(self, quantidade: int):        
        if not isinstance(quantidade, int):
            return        
        self.__quantidade_estoque += quantidade
        if self.__quantidade_estoque < 0:
            self.__quantidade_estoque = 0 