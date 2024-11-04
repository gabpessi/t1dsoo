from entidade.animal import Animal
from entidade.servico import Servico

class Consulta:
    def __init__(self, data: str, horario:str, descricao: str, animal: Animal, servico: Servico, codigo: str):
        if isinstance(animal, Animal):
            self.__animal = animal
        if isinstance(servico, Servico):
            self.__servico = servico
        self.__data = data
        self.__horario = horario
        self.__descricao = descricao        
        self.__codigo = codigo

    @property 
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):       
       self.__data = data

    @property 
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario: str):       
       self.__horario = horario

    @property 
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):       
       self.__descricao = descricao

    @property 
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal):
       if isinstance(animal, Animal):            
        self.__animal = animal

    @property 
    def servico(self):
        return self.__servico

    @servico.setter
    def servico(self, servico):
       if isinstance(servico, Servico):          
        self.__servico = servico

    @property 
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str):      
       self.__codigo = codigo

    