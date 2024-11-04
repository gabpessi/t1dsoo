import uuid
from datetime import datetime
from entidade.cliente import Cliente


class Venda:
    def __init__(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        self.__data = datetime.now()
        self.__codigo_venda = str(uuid.uuid4())
        self.__produtos = []
        self.__valor_total = 0.0

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
    def valor_total(self, valor_total: int):        
            self.__valor_total = valor_total

    @property
    def codigo_venda(self):
        return self.__codigo_venda 
