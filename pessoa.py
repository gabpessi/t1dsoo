class Pessoa():
    def __init__(self, nome: str, telefone: int, email:str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
       if not isinstance(nome, str):
            return
       self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
       if not isinstance(telefone, int):
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
    
   