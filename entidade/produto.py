class Produto:
    def __init__(self, nome: str, preco: int, codigo: str, quantidade_estoque: int):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):       
       self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco: int):       
       self.__preco = preco    

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str):       
       self.__codigo = codigo

    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade_estoque: int):       
       self.__quantidade_estoque = quantidade_estoque
       

    def atualizar_estoque(self, quantidade):
        try:

            quantidade_estoque = int(self.__quantidade_estoque)

            if quantidade_estoque + quantidade >= 0:
                self.__quantidade_estoque = quantidade_estoque + quantidade
                return True
            else:
                return False
        except ValueError:
            raise ValueError("Erro: A quantidade em estoque não é um número válido.")

    