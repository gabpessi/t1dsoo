from limite.abstract_tela import AbstractTela

class TelaSistema(AbstractTela):
   def __init__(self) -> None:
        pass
   
   def tela_opcoes(self):
      print("-------- Sistema Petshop ---------")
      print("Escolha sua opcao")
      print("1 - Serviços")
      print("2 - Produtos")     
      print("3 - Clientes")
      print("4 - Consultas")   
      print("5 - Veterinários")
      print("6 - Vendas")
      print("0 - Encerrar Sistema")

      opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,5,6,0])
      return opcao
