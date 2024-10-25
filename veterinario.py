from pessoa import Pessoa
from consulta import Consulta
from animal import Animal
from servico import Servico

class Veterinario(Pessoa):
    def __init__(self, nome:str, telefone:int, email: str, especialidade: str, cpf: str):
        super().__init__(nome, telefone, email, cpf)        
        self.__especialidade = especialidade
        self.__consultas = []

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
       if not isinstance(especialidade, str):
            return
       self.__especialidade = especialidade   

    @property
    def consultas(self):
        return self.__consultas

    @consultas.setter
    def consultas(self, consultas):
       if not isinstance(consultas, str):
            return
       self.__consultas = consultas    

    def adicionar_consulta(self, consulta: Consulta):
        if consulta in self.__consultas:
            return
        self.__consultas.append(consulta)

    def remover_consulta(self, consulta: Consulta):
        self.__consultas.remove(consulta)
        
    