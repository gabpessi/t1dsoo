from abc import ABC, abstractmethod
class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, telefone: str, email: str, cpf: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__cpf = cpf    

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):       
       self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):       
       self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):       
       self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):       
       self.__email = email
    
   