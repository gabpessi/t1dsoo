from animal import Animal
from pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome:str, telefone:int, email: str):
        super().__init__(nome, telefone, email)
        self.animais = []

    def adicionar_animal(self, animal: Animal):
        if not isinstance(animal, Animal):
            return
        self.animais.append(animal)

    def remover_animal(self, animal: Animal):
        self.animais.remove(animal)

    def listar_animais(self):
        return [animal.nome for animal in self.animais]


        