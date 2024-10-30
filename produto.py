class Produto:
    def __init__(self, nome: str, preco: int, codigo: int, quantidade_estoque: int):
        self.__codigo = codigo
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
       if not isinstance(self, int):
            return
       self.__preco = preco    

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
       if not isinstance(codigo, int):
            return
       self.__codigo = codigo

    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade_estoque):
       if not isinstance(quantidade_estoque, int):
            return
       self.__quantidade_estoque = quantidade_estoque
       

    def atualizar_estoque(self, quantidade):
        if self.__quantidade_estoque + quantidade >= 0:
            self.__quantidade_estoque += quantidade
            return True
        else:
            print("Quantidade insuficiente em estoque.")
            return False
    