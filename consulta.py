from animal import Animal
from servico import Servico


class Consulta:
    def __init__(self, data: str, horario:str, descricao: str, animal: Animal, servico: Servico, codigo: str):
        self.__data = data
        self.__horario = horario
        self.__descricao = descricao
        self.__animal = animal
        self.__servico = servico
        self.__codigo = codigo

    @property 
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
       if not isinstance(data, str):
            return
       self.__data = data

    @property 
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
       if not isinstance(horario, str):
            return
       self.__horario = horario

    @property 
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
       if not isinstance(descricao, str):
            return
       self.__descricao = descricao

    @property 
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal):
       if not isinstance(animal, Animal):
            return
       self.__animal = animal

    @property 
    def servico(self):
        return self.__servico

    @servico.setter
    def servico(self, servico):
       if not isinstance(servico, Servico):
            return
       self.__servico = servico

    @property 
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
       if not isinstance(codigo, str):
            return
       self.__codigo = codigo

    