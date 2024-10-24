class TelaProduto():  
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado  
  def tela_opcoes(self):
    print("-------- PRODUTOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Produto")
    print("2 - Alterar Produto")
    print("3 - Listar Produto")
    print("4 - Excluir Produto")
    print("5 - Verificar Disponibilidade")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    if not isinstance(opcao, int):
      print("Dados em formato errado")
      return
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_produto(self):
    print("-------- DADOS PRODUTO ----------")
    nome = input("Nome: ")
    preco = int(input("Preco: "))
    codigo = int(input("Codigo: "))
    quantidade_estoque = int(input("Quantidade Estoque: "))
    if not isinstance(nome, str) or not isinstance(preco, int) or not isinstance(codigo, int) or not isinstance(quantidade_estoque, int):
      print("Dados em formato incorreto")
      return

    return {"nome": nome, "preco": preco, "codigo": codigo, "quantidade_estoque": quantidade_estoque}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_produto(self, dados_produto):
    print("NOME DO PRODUTO: ", dados_produto["nome"])
    print("PRECO DO PRODUTO: ", dados_produto["preco"])
    print("CODIGO DO PRODUTO: ", dados_produto["codigo"])
    print("QUANTIDADE DO PRODUTO: ", dados_produto["quantidade_estoque"])    
    print("\n")
    
    if not isinstance(dados_produto["nome"], str) or not isinstance(dados_produto["preco"], int) or not isinstance(dados_produto["codigo"], int) or not isinstance(dados_produto["quantidade_estoque"], int):
      print("Dados em formato incorreto")
      return

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_produto(self):
    codigo = int(input("Código do produto que deseja selecionar: "))
    if not isinstance(codigo, int):
      print("Dados em forma incorreta")
      return
    
    return codigo
  

  def mostra_mensagem(self, msg):
    print(msg)