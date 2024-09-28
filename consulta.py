from animal import Animal
from servico import Servico


class Consulta:
    def __init__(self, data: str, horario:str, descricao: str, animal: Animal, servico: Servico):
        self.__data = data
        self.__horario = horario
        self.__descricao = descricao
        self.__animal = animal
        self.__servico = servico

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

    def exibir_detalhes(self):
        return f"Consulta em {self.__data} no horário {self.__horario} para {self.__animal.nome}. Descrição: {self.__descricao}. Serviço: {self.__servico.nome}."