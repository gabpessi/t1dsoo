from animal import Animal
from cliente import Cliente
from consulta import Consulta
from tela_consulta import TelaConsulta

class TelaVeterinario():  
  def __init__(self):
        self.__tela_consulta = TelaConsulta()
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado  
  def tela_opcoes(self):
    print("-------- VETERINARIOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Veterinário")
    print("2 - Alterar Veterinário")
    print("3 - Listar Veterinário")
    print("4 - Excluir Veterinário")   
    print("5 - Adicionar Consulta") 
    print("6 - Remover Consulta") 
    print("7 - Listar Consulta")    
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    if not isinstance(opcao, int):
      print("Dados em formato errado")
      return
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_veterinario(self):
    print("-------- DADOS VETERINARIO ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    cpf = input("CPF: ")
    especialidade = input("Especialidade: ")
   
    if not isinstance(nome, str) or not isinstance(telefone, str) or not isinstance(email, str) or not isinstance(cpf, str) or not isinstance(especialidade, str):
        print("Dados em formato incorreto.")
        return

    return {"nome": nome, "telefone": telefone, "email": email, "cpf": cpf, "especialidade": especialidade}

  def pega_codigo_consulta(self):
        codigo = input("Digite o código da consulta: ")
        return codigo  
  
  def seleciona_veterinario(self):
    cpf = input("Cpf do veterinário que deseja selecionar: ")
    if not isinstance(cpf, str):
      print("Dados em forma incorreta")
      return
    
    return cpf
  
  def mostra_consulta(self, dados_consulta):
    if not dados_consulta:
        print("Nenhuma consulta disponível.")
        return
    
    for consulta in dados_consulta:        
        print("DATA DA CONSULTA: ", consulta.data)
        print("HORARIO DA CONSULTA: ", consulta.horario)
        print("DESCRICAO DA CONSULTA: ", consulta.descricao)
        print("ANIMAL DA CONSULTA: ", consulta.animal)
        print("SERVICO DA CONSULTA: ", consulta.servico)
        print("CODIGO DA CONSULTA: ", consulta.codigo)
        print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_veterinario(self, dados_veterinario):
    print("NOME DO VETERINARIO: ", dados_veterinario["nome"])
    print("TELEFONE DO VETERINARIO: ", dados_veterinario["telefone"])
    print("EMAIL DO VETERINARIO: ", dados_veterinario["email"])
    print("CPF DO VETERINARIO: ", dados_veterinario["cpf"])  
    print("ESPECIALIDADE DO VETERINARIO"), dados_veterinario["especialidade"]    
    
    if "consultas" in dados_veterinario and dados_veterinario["consultas"]:
        print("CONSULTAS DO VETERINARIO: ")
        
        for consulta in dados_veterinario["consultas"]:
            if isinstance(consulta, Consulta):
                print(f"Data: {consulta.data}, código da consulta: {consulta.codigo}")
                
            else:
               print("Dados em formato incorreto")
    else:
        print("Este veterinário não possui consultas cadastradas.")

    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_veterinario(self):
    cpf = input("Cpf do veterinário que deseja selecionar: ")
    if not isinstance(cpf, str):
      print("Dados em forma incorreta")
      return
    
    return cpf
  

  def mostra_mensagem(self, msg):
    print(msg)