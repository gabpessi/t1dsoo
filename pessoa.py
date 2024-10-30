from abc import ABC, abstractmethod
class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, telefone: str, email:str, cpf: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__cpf = cpf    

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
       if not isinstance(nome, str):
            return
       self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
       if not isinstance(cpf, str):
            return
       self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
       if not isinstance(telefone, str):
            return
       self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
       if not isinstance(email, str):
            return
       self.__email = email
    
   