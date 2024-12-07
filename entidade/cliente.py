from entidade.pessoa import Pessoa
from entidade.animal import Animal
from exceptions.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException

class Cliente(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, cpf: str):
        super().__init__(nome, telefone, email, cpf)
        self.__animais = []

    @property
    def animais(self):
        return self.__animais
    
    
    def adicionar_animal(self, nome_animal: str, especie: str, raca: str, idade: int, numero_cadastro: str):
        novo_animal = Animal(nome_animal, especie, raca, idade, numero_cadastro)
        self.__animais.append(novo_animal)
        
    
    def remover_animal(self, numero_cadastro: str):
        for animal in self.__animais:
            if animal.numero_cadastro == numero_cadastro:
                self.__animais.remove(animal)
                return
        raise ObjetoNaoEncontradoException("Animal")