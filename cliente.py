from animal import Animal
from pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome:str, telefone:int, email: str, cpf: str):
        super().__init__(nome, telefone, email, cpf)
        self.__animais = []

    @property
    def animais(self):
        return self.__animais
    
    @animais.setter
    def animais(self, animal):
        if isinstance(animal, Animal):
            self.__animais.append(animal)
        

  
        