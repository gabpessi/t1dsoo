from entidade.pessoa import Pessoa
from entidade.consulta import Consulta

class Veterinario(Pessoa):
    def __init__(self, nome:str, telefone:int, email: str, cpf: str, especialidade: str):
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
    
    def adicionar_consulta(self, consulta: Consulta):
        if consulta in self.__consultas:
            return
        self.__consultas.append(consulta)

    def remover_consulta(self, consulta: Consulta):
        if consulta in self.__consultas:
            self.__consultas.remove(consulta)
        
    