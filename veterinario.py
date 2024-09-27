from pessoa import Pessoa
from consulta import Consulta
from animal import Animal
from servico import Servico

class Veterinario(Pessoa):
    def __init__(self, nome:str, telefone:int, email: str, especialidade: str, consultas: Consulta):
        super().__init__(nome, telefone, email)
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

    def marcar_consulta(self, data: str, descricao: str, animal: Animal, servico: Servico):
        consulta = Consulta(self, data, descricao, animal, servico)
        if consulta in self.__consultas:
            return
        self.__consultas.append(consulta)
