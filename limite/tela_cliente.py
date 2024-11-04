from limite.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):  
  def __init__(self) -> None:
        pass

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

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,5,6,7,8,0])
    return opcao

  
  def pega_dados_cliente(self):    
    print("-------- DADOS CLIENTE ----------")        
    nome = self.le_string_com_tamanho("Nome: ", min_tamanho=2, campo="nome", somente_letras=True)
    telefone = self.le_string_com_tamanho("Telefone: ", min_tamanho=9, campo="telefone", somente_digitos=True)
    email = self.le_email("Email: ")
    cpf = self.le_string_com_tamanho("CPF: ", min_tamanho=11, max_tamanho=11, campo="CPF", somente_digitos=True)

    return {"nome": nome, "telefone": telefone, "email": email, "cpf": cpf}


  def mostra_cliente(self, dados_cliente):
    print("NOME DO CLIENTE: ", dados_cliente["nome"])
    print("TELEFONE DO CLIENTE: ", dados_cliente["telefone"])
    print("EMAIL DO CLIENTE: ", dados_cliente["email"])
    print("CPF DO CLIENTE: ", dados_cliente["cpf"])    
    if "animais" in dados_cliente and dados_cliente["animais"]:
        print("ANIMAIS DO CLIENTE: ")
        
        for animal in dados_cliente["animais"]:            
            print(f"Nome: {animal.nome_animal}, número de cadastro: {animal.numero_cadastro}")
                
            
    else:
        print("Este cliente não possui animais cadastrados.")

    print("\n")


  def seleciona_cliente(self):
    cpf = self.le_string_com_tamanho("CPF do Cliente: ", min_tamanho=11, max_tamanho=11, campo="CPF", somente_digitos=True)
    return cpf

  
  def seleciona_animal(self):
    numero_cadastro = self.le_string_com_tamanho("Número de cadastro do animal: ", somente_digitos=True)
    return numero_cadastro
  
  def pega_dados_animal(self):
    print("-------- DADOS DO ANIMAL ----------")    
    nome_animal = self.le_string_com_tamanho("Nome do Animal: ", min_tamanho=2, campo="Nome do Animal", somente_letras=True)    
    especie = self.le_string_com_tamanho("Espécie: ", min_tamanho=3, campo="Espécie", somente_letras=True)
    raca = self.le_string_com_tamanho("Raça: ", min_tamanho=3, campo="Raça", somente_letras=True) 
    idade = self.le_num_inteiro("Idade: ", ints_validos=range(0, 101))       
    numero_cadastro = self.le_string_com_tamanho("Número de Cadastro: ", campo="Número de Cadastro", somente_digitos=True)

    return {
        "nome_animal": nome_animal,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "numero_cadastro": numero_cadastro
    }

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