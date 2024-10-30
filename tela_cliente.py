from animal import Animal
from cliente import Cliente

class TelaCliente():  
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado  
  def tela_opcoes(self):
    print("-------- CLIENTES ----------")
    print("Escolha a opcao")
    print("1 - Incluir Cliente")
    print("2 - Alterar Cliente")
    print("3 - Listar Cliente")
    print("4 - Excluir Cliente")   
    print("5 - Incluir Animal") 
    print("6 - Alterar Animal") 
    print("7 - Excluir Animal") 
    print("8 - Listar Animal")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    if not isinstance(opcao, int):
      print("Dados em formato errado")
      return
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_cliente(self):
    print("-------- DADOS CLIENTE ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    cpf = input("CPF: ")
   
    if not isinstance(nome, str) or not isinstance(telefone, str) or not isinstance(email, str) or not isinstance(cpf, str):
        print("Dados em formato incorreto.")
        return

    return {"nome": nome, "telefone": telefone, "email": email, "cpf": cpf}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_cliente(self, dados_cliente):
    print("NOME DO CLIENTE: ", dados_cliente["nome"])
    print("TELEFONE DO CLIENTE: ", dados_cliente["telefone"])
    print("EMAIL DO CLIENTE: ", dados_cliente["email"])
    print("CPF DO CLIENTE: ", dados_cliente["cpf"])    
    if "animais" in dados_cliente and dados_cliente["animais"]:
        print("ANIMAIS DO CLIENTE: ")
        
        for animal in dados_cliente["animais"]:
            if isinstance(animal, Animal):
                print(f"Nome: {animal.nome_animal}, número de cadastro: {animal.numero_cadastro}")
                
            else:
               print("Dados em formato incorreto")
    else:
        print("Este cliente não possui animais cadastrados.")

    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_cliente(self):
    cpf = input("Cpf do cliente que deseja selecionar: ")
    if not isinstance(cpf, str):
      print("Dados em forma incorreta")
      return
    
    return cpf
  
  def seleciona_animal(self):
    numero_cadastro = input("Número de cadastro do animal que deseja selecionar: ")
    if not isinstance(numero_cadastro, str):
      print("Dados em forma incorreta")
      return
    
    return numero_cadastro
  
  def pega_dados_animal(self):
    print("-------- DADOS DO ANIMAL ----------")
    nome_animal = input("Nome do Animal: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    idade = input("Idade: ")
    numero_cadastro = input("Número de Cadastro: ") 

    try:
        idade = int(idade)  # Converter para int
    except ValueError:
        print("Idade deve ser um número.")
        return None  # Retorna None em caso de erro

    return {"nome_animal": nome_animal, "especie": especie, "raca": raca, "idade": idade, "numero_cadastro": numero_cadastro}

  def mostra_animal(self, animal):
          print("-------- DADOS DO ANIMAL ----------")
          print(f"Nome do Animal: {animal.nome_animal}")
          print(f"Espécie: {animal.especie}")
          print(f"Raça: {animal.raca}")
          print(f"Idade: {animal.idade}")
          print(f"Número de Cadastro: {animal.numero_cadastro}")
          print("\n")

  def mostra_mensagem(self, msg):
    print(msg)