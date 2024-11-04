import uuid
from datetime import datetime
from limite.abstract_tela import AbstractTela

class TelaVenda(AbstractTela): 
    def __init__(self) -> None:
            pass
    
    def tela_opcoes(self):
        print("-------- VENDAS ----------")  
        print("1 - Iniciar Venda")    
        print("2 - Adicionar Produto")
        print("3 - Remover Produto")  
        print("4 - Listar Produtos da Venda Atual")      
        print("5 - Listar Vendas")
        print("6 - Finalizar Venda")           
        print("0 - Retornar")
        

        opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,5,6,0])
        return opcao
    
    
    def pega_dados_venda(self):
        print("-------- DADOS VENDA ----------")
        cpf_cliente = self.le_string_com_tamanho("CPF do Cliente: ", min_tamanho=11, max_tamanho=11, campo="CPF do Cliente", somente_digitos=True)
        codigo_produto = self.le_string_com_tamanho("Código do Produto: ", campo="Código do Produto", somente_digitos=True)
        quantidade = self.le_num_inteiro("Quantidade: ", ints_validos=range(0, 100))       
        codigo_venda = str(uuid.uuid4())
        data = datetime.now()

        return {"cpf_cliente": cpf_cliente, "codigo_produto": codigo_produto, "quantidade": quantidade, "codigo_venda": codigo_venda, "data": data}       

    def pega_quantidade_produto(self):
            quantidade = self.le_num_inteiro("Quantidade do Produto: ", ints_validos=range(0, 100))
            return quantidade

    def seleciona_produto(self):        
        codigo = self.le_string_com_tamanho("Código do Produto: ", campo="Código do Produto", somente_digitos=True)   
        return codigo
    
    def mostra_venda(self, venda):
   
        print("--------- DETALHES DA VENDA ---------")        
        print(f"Cliente: {venda.cliente.nome}")  
        print(f"CPF: {venda.cliente.cpf}")  
        print(f"Data: {venda.data.strftime('%d/%m/%Y')}")
        print(f"Código venda: {venda.codigo_venda}")
        print("Produtos:")           
        if venda.produtos:            
            for produto, quantidade in venda.produtos: 
                print(f"- {produto.nome}: {quantidade} (Código: {produto.codigo})") 
        else:
            print("Nenhum produto adicionado.")
        print(f"Valor total: R${venda.valor_total:.2f}")


    def mostra_produto_venda(self, nome_produto, quantidade):
        print(f"PRODUTO: {nome_produto}")
        print(f"QUANTIDADE: {quantidade}\n")

    def pega_periodo_relatorio(self):
        print("-------- RELATÓRIO DE VENDAS ---------")
        data_inicio_str = input("Data de Início (dd/mm/aaaa): ")
        data_fim_str = input("Data de Fim (dd/mm/aaaa): ")

        data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y")

        return data_inicio, data_fim

    def mostra_mensagem(self, mensagem):
        print(mensagem)    
    
  
    