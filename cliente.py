from animal import Animal
from pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome:str, telefone:int, email: str, cpf: str):
        super().__init__(nome, cpf, telefone, email)
        self.__animais = []

    @property
    def animais(self):
        return self.__animais
    
    @animais.setter
    def animais(self, animal):
        if isinstance(animal, Animal):
            self.__animais.append(animal)
        

    def adicionar_animal(self, nome: str, especie: str, raca: str, idade: int, petshop):
        
        animal = Animal(nome, especie, raca, idade)
        self.__animais.append(animal)
        
        petshop.registrar_animal(animal)

    def remover_animal(self, animal: Animal):
        if animal in self.__animais:
            self.__animais.remove(animal)
            del animal 

    def listar_animais(self):
        return [animal.nome for animal in self.animais]

    def __del__(self):        
        for animal in self.__animais:
            del animal
        