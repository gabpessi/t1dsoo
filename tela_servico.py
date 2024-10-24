class TelaServico():  
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado  
  def tela_opcoes(self):
    print("-------- SERVICOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Servico")
    print("2 - Alterar Servico")
    print("3 - Listar Servico")
    print("4 - Excluir Servico")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    if not isinstance(opcao, int):
      print("Dados em formato errado")
      return
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_servico(self):
    print("-------- DADOS SERVICO ----------")
    nome = input("Nome: ")
    preco = int(input("Preco: "))
    codigo = int(input("Codigo: "))
    if not isinstance(nome, str) or not isinstance(preco, int) or not isinstance(codigo, int):
      print("Dados em formato incorreto")
      return

    return {"nome": nome, "preco": preco, "codigo": codigo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_servico(self, dados_servico):
    print("NOME DO SERVICO: ", dados_servico["nome"])
    print("PRECO DO SERVICO: ", dados_servico["preco"])
    print("CODIGO DO SERVICO: ", dados_servico["codigo"])
    print("\n")
    
    if not isinstance(dados_servico["nome"], str) or not isinstance(dados_servico["preco"], int) or not isinstance(dados_servico["codigo"], int):
      print("Dados em formato incorreto")
      return

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_servico(self):
    codigo = int(input("Código do servico que deseja selecionar: "))
    if not isinstance(codigo, int):
      print("Dados em forma incorreta")
      return
    
    return codigo
  

  def mostra_mensagem(self, msg):
    print(msg)