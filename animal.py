class Animal:
    def __init__(self, nome: str, especie: str, raca: str, idade: int):
        self.__nome = nome
        self.__especie = especie
        self.__raca = raca
        self.__idade = idade

   # @property
   # def x(self):
   #     return self.__x

   # def (self, x):
   #    if not isinstance():
   #         return
    #   self.__x = x

    @property 
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
       if not isinstance(nome, str):
            return
       self.__nome = nome

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, especie):
       if not isinstance(especie, str):
            return
       self.__especie =  especie
    
    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
       if not isinstance(raca, str):
            return
       self.__raca = raca

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
       if not isinstance(idade, int):
            return
       self.__idade = idade 

    
    def incrementar_idade(self, idade):
        pass

    def adicionar_consulta(Consulta):
        pass

    def listar_consultas():
        pass