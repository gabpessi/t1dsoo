from animal import Animal
from pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome:str, telefone:int, email: str):
        super().__init__(nome, telefone, email)
        self.__animais = []

    @property
    def animais(self):
        return self.__animais
    
    @animais.setter
    def animais(self, animal):
        if isinstance(animal, Animal):
            self.__animais.append(animal)
        

    def adicionar_animal(self, animal: Animal):
        if not isinstance(animal, Animal) or animal in self.__animais:
            return
        self.animais.append(animal)

    def remover_animal(self, animal: Animal):
        self.animais.remove(animal)

    def listar_animais(self):
        return [animal.nome for animal in self.animais]


        