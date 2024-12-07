class Animal:
    def __init__(self, nome_animal: str, especie: str, raca: str, idade: int, numero_cadastro: str):
        self.__nome_animal = nome_animal
        self.__especie = especie
        self.__raca = raca
        self.__idade = idade
        self.__numero_cadastro = numero_cadastro

    @property 
    def nome_animal(self):
        return self.__nome_animal

    @nome_animal.setter
    def nome_animal(self, nome_animal: str):   
       self.__nome_animal = nome_animal

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, especie: str):                  
        self.__especie =  especie
    
    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca: str):       
       self.__raca = raca

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):   
       self.__idade = idade 

    @property
    def numero_cadastro(self):
        return self.__numero_cadastro

    @numero_cadastro.setter
    def numero_cadastro(self, numero_cadastro: str):       
       self.__numero_cadastro = numero_cadastro 

    
    

    