class Servico:
    def __init__(self, nome: str, preco: int, codigo: str):
        self.__nome = nome
        self.__preco = preco
        self.__codigo = codigo

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