from pessoa import Pessoa
class Veterinario(Pessoa):
    def __init__(self, nome:str, telefone:int, email: str, especialidade: str):
        super().__init__(nome, telefone, email)
        self.__especialidade = especialidade

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
       if not isinstance(especialidade, str):
            return
       self.__especialidade = especialidade