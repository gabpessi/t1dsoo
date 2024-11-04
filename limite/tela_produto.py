from limite.abstract_tela import AbstractTela
class TelaProduto(AbstractTela):
  def __init__(self) -> None:
        pass

  def tela_opcoes(self):
    print("-------- PRODUTOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Produto")
    print("2 - Alterar Produto")
    print("3 - Listar Produto")
    print("4 - Excluir Produto")
    print("5 - Verificar Disponibilidade")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,5,0])
    return opcao
  
  def pega_dados_produto(self):
    print("-------- DADOS PRODUTO ----------")
    nome = self.le_string_com_tamanho("Nome: ", min_tamanho=2, campo="nome", somente_letras=True)
    preco = self.le_num_inteiro("Preco: ", ints_validos=range(0, 10001)) 
    codigo = self.le_string_com_tamanho("Código do Produto: ", campo="Código do Produto", somente_digitos=True)
    quantidade_estoque = self.le_num_inteiro("Quantidade Estoque: ", ints_validos=range(0, 10001))    

    return {"nome": nome, "preco": preco, "codigo": codigo, "quantidade_estoque": quantidade_estoque}

  def mostra_produto(self, dados_produto):
    print("NOME DO PRODUTO: ", dados_produto["nome"])
    print("PRECO DO PRODUTO: ", dados_produto["preco"])
    print("CODIGO DO PRODUTO: ", dados_produto["codigo"])
    print("QUANTIDADE DO PRODUTO: ", dados_produto["quantidade_estoque"])    
    print("\n")

  def seleciona_produto(self):
    codigo = self.le_string_com_tamanho("Código do Produto: ", campo="Código do Produto", somente_digitos=True)
    return codigo
  

  def mostra_mensagem(self, msg):
    print(msg)