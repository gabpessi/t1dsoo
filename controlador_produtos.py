from tela_produto import TelaProduto
from produto import Produto

class ControladorProdutos():
    def __init__(self, controlador_sistema):
        self.__produtos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()

    def pega_produto_por_codigo(self, codigo: int):
        for produto in self.__produtos:
            if(produto.codigo == codigo):
                return produto
        return None

    def incluir_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()        
        s = self.pega_produto_por_codigo(dados_produto["codigo"])
        if s is None:
            produto = Produto(dados_produto["nome"], dados_produto["preco"], dados_produto["codigo"], dados_produto["quantidade_estoque"])
            self.__produtos.append(produto)
        else:
            self.__tela_produto.mostra_mensagem("ATENÇÃO: Produto já cadastrado")

    def alterar_produto(self):
        self.lista_produto()
        codigo_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo(codigo_produto)

        if(produto is not None):
            novos_dados_produto = self.__tela_produto.pega_dados_produto()
            produto.nome = novos_dados_produto["nome"]
            produto.preco = novos_dados_produto["preco"]
            produto.codigo = novos_dados_produto["codigo"]
            produto.quantidade_estoque = novos_dados_produto["quantidade_estoque"]
            self.lista_produto()
        else:
            self.__tela_produto.mostra_mensagem("ATENCAO: produto não cadastrado")

# Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_produto(self):
        for produto in self.__produtos:
            self.__tela_produto.mostra_produto({"nome": produto.nome, "preco": produto.preco, "codigo": produto.codigo, "quantidade_estoque": produto.quantidade_estoque})

    def excluir_produto(self):
        self.lista_produto()
        codigo_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo(codigo_produto)

        if(produto is not None):
            self.__produtos.remove(produto)
            self.lista_produto()
        else:
            self.__tela_produto.mostra_mensagem("ATENCÃO: produto não existente")

    def verificar_disponibilidade(self: bool): 
        self.lista_produto()
        codigo_produto = self.__tela_produto.seleciona_produto()  
        produto = self.pega_produto_por_codigo(codigo_produto)
        
        if(produto is not None):
            self.__tela_produto.mostra_mensagem(f"Produto disponível em {produto.quantidade_estoque} unidades")
        else:
            self.__tela_produto.mostra_mensagem("Produto não disponível")        
   

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_produto, 2: self.alterar_produto, 3: self.lista_produto, 4: self.excluir_produto, 5:self.verificar_disponibilidade, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_produto.tela_opcoes()]()