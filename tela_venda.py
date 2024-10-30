import uuid
from datetime import datetime
class TelaVenda: 

    def tela_opcoes(self):
        print("-------- VENDAS ----------")  
        print("1 - Iniciar Venda")    
        print("2 - Adicionar Produto")
        print("3 - Remover Produto")        
        print("4 - Listar Vendas")
        print("5 - Finalizar Venda")           
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        if not isinstance(opcao, int):
            print("Dados em formato errado")
            return
        
        return opcao
    
    def pega_quantidade_produto(self):
        quantidade = int(input("Digite a quantidade: "))
        return quantidade

    def pega_dados_venda(self):
        print("-------- DADOS VENDA ----------")
        cpf_cliente = input("CPF do cliente: ")
        codigo_produto = input("Código produto: ")
        quantidade = int(input("Quantidade: "))
        codigo_venda = str(uuid.uuid4())
        data = datetime.now()

        return {"cpf_cliente": cpf_cliente, "codigo_produto": codigo_produto, "quantidade": quantidade, "codigo_venda": codigo_venda, "data": data}

        
    def pega_dados_produto(self):
        codigo_produto = input("Digite o código do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        
        # Busca o produto pelo código
        produto = self.__controlador_produtos.pega_produto_por_codigo(codigo_produto)
        
        if produto is None:
            print("Produto não encontrado.")
            return None, 0  # Retorna None e 0 para indicar que não foi encontrado
        
        return produto, quantidade
    
    def seleciona_venda(self):
        codigo = str(uuid.uuid4())
        if not isinstance(codigo, str):
            print("Dados em forma incorreta")
            return
        
        return codigo

    def seleciona_produto(self):
        try:
            codigo = input("Código do produto: ")
        except ValueError:
            print("Código inválido. Por favor, insira um número.")
            return None
        return codigo
    
    def mostra_venda(self, venda):
    # Exibir informações sobre a venda
        print("--------- DETALHES DA VENDA ---------")        
        print(f"Cliente: {venda.cliente.nome}")  
        print(f"CPF: {venda.cliente.cpf}")  
        print(f"Data: {venda.data}")
        print(f"Código venda: {venda.codigo_venda}")
        print("Produtos:")           
        if venda.produtos:            
            for produto, quantidade in venda.produtos:  # Desempacota a tupla
                print(f"- {produto.nome}: {quantidade} (Código: {produto.codigo})")  # Exibe o código do produto e a quantidade
        else:
            print("Nenhum produto adicionado.")
        print(f"Valor total: R${venda.valor_total:.2f}")


    def mostra_produto(self, dados_produto):
        print("NOME DO PRODUTO: ", dados_produto["nome"])
        print("CODIGO DO PRODUTO: ", dados_produto["codigo"])
        print("QUANTIDADE: ", dados_produto["quantidade"])        
        print("PREÇO: R$", dados_produto["preco"])

    def mostra_mensagem(self, mensagem):
        print(mensagem)    
    
    
    def seleciona_codigo_venda(self):
        # Solicitar ao usuário que insira o código da venda
        codigo_venda = input("Digite o código da venda que deseja selecionar: ")
        return codigo_venda
    
    