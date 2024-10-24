from animal import Animal
from servico import Servico

class TelaConsulta():  
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado  
  def tela_opcoes(self):
    print("-------- CONSULTAS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Consulta")
    print("2 - Alterar Consulta")
    print("3 - Listar Consulta")
    print("4 - Excluir Consulta")   
    print("5 - Exibir Detalhes") 
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    if not isinstance(opcao, int):
      print("Dados em formato errado")
      return
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_consulta(self):
    print("-------- DADOS CONSULTA ----------")
    data = input("Data: ")
    horario = input("Horario: ")
    descricao = input("Descricao: ")
    animal = input("Animal: ")
    servico = input("Serviço: ")
    codigo = int(input("Codigo: "))
    if not isinstance(data, str) or not isinstance(descricao, str) or not isinstance(animal, str) or not isinstance(servico, str) or not isinstance(codigo, int):
      print("Dados em formato incorreto")
      return

    return {"data": data, "horario": horario, "descricao": descricao, "animal": animal, "servico": servico, "codigo": codigo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_consulta(self, dados_consulta):
    print("DATA DA CONSULTA: ", dados_consulta["data"])
    print("HORARIO DA CONSULTA: ", dados_consulta["horario"])
    print("DESCRICAO DA CONSULTA: ", dados_consulta["descricao"])
    print("ANIMAL DA CONSULTA: ", dados_consulta["animal"])    
    print("SERVICO DA CONSULTA: ", dados_consulta["servico"])    
    print("CODIGO DA CONSULTA: ", dados_consulta["codigo"])    
    print("\n")
    
    if not isinstance(dados_consulta["data"], str) or not isinstance(dados_consulta["horario"], str) or not isinstance(dados_consulta["descricao"], str) or not isinstance(dados_consulta["animal"], str) or not isinstance(dados_consulta["servico"], str or not isinstance(dados_consulta["codigo"], int)):
      print("Dados em formato incorreto")
      return

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_consulta(self):
    codigo = int(input("Código da consulta que deseja selecionar: "))
    if not isinstance(codigo, int):
      print("Dados em forma incorreta")
      return
    
    return codigo
  

  def mostra_mensagem(self, msg):
    print(msg)