from datetime import datetime
import uuid
from tela_venda import TelaVenda
from tela_cliente import TelaCliente 
from venda import Venda
from cliente import Cliente

from tela_venda import TelaVenda
from venda import Venda
from tela_produto import TelaProduto
from tela_venda import TelaVenda
from venda import Venda

class ControladorVendas():
    def __init__(self, controlador_sistema, controlador_produtos, controlador_clientes):        
        self.__vendas = []            
        self.__controlador_sistema = controlador_sistema
        self.__tela_venda = TelaVenda()
        self.__tela_cliente = TelaCliente()
        self.__tela_produto = TelaProduto()
        self.__controlador_produtos = controlador_produtos 
        self.__controlador_clientes = controlador_clientes
        self.__venda_atual = None  # Venda ativa no momento

    def iniciar_venda(self):
        if self.__venda_atual:  # Verifica se já existe uma venda ativa
            self.__tela_venda.mostra_mensagem("Uma venda já está em andamento. Finalize a venda atual antes de iniciar uma nova.")
            return
        cpf_cliente = self.__tela_cliente.seleciona_cliente()  # Solicita o CPF do cliente
        cliente = self.__controlador_clientes.pega_cliente_por_cpf(cpf_cliente)
        
        if cliente:
            self.__venda_atual = Venda(cliente)  # Cria nova venda e gera código automaticamente
            self.__venda_atual.produtos.clear()
            self.__venda_atual.valor_total = 0.0
            self.__tela_venda.mostra_mensagem(f"Nova venda iniciada para {cliente.nome}.")
        else:
            self.__tela_venda.mostra_mensagem("Cliente não encontrado.")

    def adicionar_produto(self):
        if not self.__venda_atual:
            self.__tela_venda.mostra_mensagem("Nenhuma venda ativa. Inicie uma nova venda primeiro.")
            return

        codigo_produto = self.__tela_venda.seleciona_produto()  # Solicita código do produto
        produto = self.__controlador_produtos.pega_produto_por_codigo(codigo_produto)

        if produto:
            quantidade = self.__tela_venda.pega_quantidade_produto()  # Solicita a quantidade
            sucesso = self.__venda_atual.adicionar_produto(produto, quantidade)
            if sucesso:
                self.__tela_venda.mostra_mensagem("Produto adicionado com sucesso à venda atual.")
            else:
                self.__tela_venda.mostra_mensagem("Quantidade do produto não é suficiente.")
        else:
            self.__tela_venda.mostra_mensagem("Produto não encontrado.")



    def remover_produto(self):
        if not self.__venda_atual:
            self.__tela_venda.mostra_mensagem("Nenhuma venda ativa. Inicie uma nova venda primeiro.")
            return

        codigo_produto = self.__tela_produto.seleciona_produto()  
        produto = self.__controlador_produtos.pega_produto_por_codigo(codigo_produto)

        if produto:
            sucesso = self.__venda_atual.remover_produto(produto)
            if sucesso:
                self.__tela_venda.mostra_mensagem("Produto removido com sucesso da venda atual.")
            else:
                self.__tela_venda.mostra_mensagem("Produto não encontrado na venda atual.")
        else:
            self.__tela_venda.mostra_mensagem("Produto não encontrado.")

    def finalizar_venda(self):
        if not self.__venda_atual:
            self.__tela_venda.mostra_mensagem("Nenhuma venda ativa para finalizar.")
            return        

        if not self.__venda_atual.produtos:
            self.__tela_venda.mostra_mensagem("Não é possível finalizar uma venda sem produtos.")
            return

        mensagem = self.__venda_atual.finalizar_venda()
        self.__vendas.append(self.__venda_atual)  # Registra a venda
        self.__tela_venda.mostra_mensagem(mensagem)  # Mostra a mensagem retornada
        self.__venda_atual = None  # Limpa a venda ativa

    def lista_venda(self):
        for venda in self.__vendas:                       
            self.__tela_venda.mostra_venda(venda)
        

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.iniciar_venda, 
            2: self.adicionar_produto, 
            3: self.remover_produto, 
            4: self.lista_venda, 
            5: self.finalizar_venda, 
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_venda.tela_opcoes()]()
