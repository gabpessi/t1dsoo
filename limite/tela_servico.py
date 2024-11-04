from limite.abstract_tela import AbstractTela

class TelaServico(AbstractTela):  
  def __init__(self) -> None:
        pass
  
  def tela_opcoes(self):
    print("-------- SERVICOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Servico")
    print("2 - Alterar Servico")
    print("3 - Listar Servico")
    print("4 - Excluir Servico")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,0])
    return opcao

  def pega_dados_servico(self):
    print("-------- DADOS SERVICO ----------")
    nome = self.le_string_com_tamanho("Nome: ", min_tamanho=2, campo="nome", somente_letras=True)
    preco = self.le_num_inteiro("Preco: ", ints_validos=range(0, 10001)) 
    codigo = self.le_string_com_tamanho("Código do Servico: ", campo="Código do Servico", somente_digitos=True)    
    return {"nome": nome, "preco": preco, "codigo": codigo}


  def mostra_servico(self, dados_servico):
    print("NOME DO SERVICO: ", dados_servico["nome"])
    print("PRECO DO SERVICO: ", dados_servico["preco"])
    print("CODIGO DO SERVICO: ", dados_servico["codigo"])
    print("\n")   


  def seleciona_servico(self):
    codigo = self.le_string_com_tamanho("Código do Servico: ", campo="Código do Servico", somente_digitos=True)   
    return codigo
  

  def mostra_mensagem(self, msg):
    print(msg)