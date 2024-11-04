from limite.tela_produto import TelaProduto
from entidade.produto import Produto
from exceptions.lista_vazia_exception import ListaVaziaException
from exceptions.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exceptions.objeto_repetido_exception import ObjetoRepetidoException

class ControladorProdutos():
    def __init__(self, controlador_sistema):
        self.__produtos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()

    def pega_produto_por_codigo(self, codigo: str):        
        for produto in self.__produtos:
            if(produto.codigo == codigo):
                return produto
        return None
    
    def seleciona_produto(self):
        return self.__tela_produto.seleciona_produto()

    def incluir_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()
        codigo = dados_produto["codigo"]        
        produto = self.pega_produto_por_codigo(codigo)
        try:
            if produto == None:
                produto = Produto(dados_produto["nome"], dados_produto["preco"], dados_produto["codigo"], dados_produto["quantidade_estoque"])
                self.__produtos.append(produto)
            else:
                raise ObjetoRepetidoException("Código do produto", codigo)
        except ListaVaziaException as e:
            self.__tela_produto.mostra_mensagem(e)
            return                  
        except ObjetoRepetidoException as e: 
            self.__tela_produto.mostra_mensagem(e)   


    def alterar_produto(self):
        try:
            if not self.__produtos:
                raise ListaVaziaException("produtos") 
            self.lista_produto()
            codigo_produto = self.__tela_produto.seleciona_produto()
            produto = self.pega_produto_por_codigo(codigo_produto)

            if produto is not None:
                novos_dados_produto = self.__tela_produto.pega_dados_produto()
                produto.nome = novos_dados_produto["nome"]
                produto.preco = novos_dados_produto["preco"]
                produto.codigo = novos_dados_produto["codigo"]
                produto.quantidade_estoque = novos_dados_produto["quantidade_estoque"]
                self.lista_produto()
            else:
                raise ObjetoNaoEncontradoException("Produto")
            
        except ListaVaziaException as e:
            self.__tela_produto.mostra_mensagem(e) 
            return  
        except ObjetoNaoEncontradoException as e:
            self.__tela_produto.mostra_mensagem(e)    


    def lista_produto(self):
        try:
            if not self.__produtos:
                raise ListaVaziaException("produtos")
            for produto in self.__produtos:
                self.__tela_produto.mostra_produto({"nome": produto.nome, "preco": produto.preco, "codigo": produto.codigo, "quantidade_estoque": produto.quantidade_estoque})

        except ListaVaziaException as e:
            self.__tela_produto.mostra_mensagem(e)

    def excluir_produto(self):
        try:
            if not self.__produtos:
                raise ListaVaziaException("produtos")
            self.lista_produto()
            codigo_produto = self.__tela_produto.seleciona_produto()
            produto = self.pega_produto_por_codigo(codigo_produto)

            if produto is not None:
                self.__produtos.remove(produto)
                self.lista_produto()
            else:
                raise ObjetoNaoEncontradoException("Produto")
            
        except ObjetoNaoEncontradoException as e:
            self.__tela_produto.mostra_mensagem(e)
        except ListaVaziaException as e:
            self.__tela_produto.mostra_mensagem(e)


    def verificar_disponibilidade(self):
        try:
            if not self.__produtos:
                raise ListaVaziaException("produtos")
            self.lista_produto()
            codigo_produto = self.__tela_produto.seleciona_produto()  
            produto = self.pega_produto_por_codigo(codigo_produto)

            if produto:
                self.__tela_produto.mostra_mensagem(f"Produto disponível em {produto.quantidade_estoque} unidades")
            else:
                raise ObjetoNaoEncontradoException("Produto") 
             
        except ObjetoNaoEncontradoException as e:
            self.__tela_produto.mostra_mensagem(e)
        except ListaVaziaException as e:
            self.__tela_produto.mostra_mensagem(e)
      
    
   

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_produto, 2: self.alterar_produto, 3: self.lista_produto, 4: self.excluir_produto, 5:self.verificar_disponibilidade, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_produto.tela_opcoes()]()