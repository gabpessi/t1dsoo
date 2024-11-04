from entidade.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, cpf: str):
        super().__init__(nome, telefone, email, cpf)
        self.__animais = []

    @property
    def animais(self):
        return self.__animais
    
    
  
        