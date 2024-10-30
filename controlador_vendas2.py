from datetime import datetime
import uuid
from tela_venda import TelaVenda
from tela_cliente import TelaCliente 
from venda import Venda
from cliente import Cliente

class ControladorVendas():
    def __init__(self, cliente: Cliente, controlador_sistema):        
        self.__vendas = []    
        self.__controlador_sistema = controlador_sistema
        self.__tela_venda = TelaVenda()

    def pega_venda_por_codigo(self, codigo):
        for venda in self.__vendas:
            if(venda.codigo == codigo):
                return codigo
        return None
        


    def adicionar_produto(self):
        dados_venda = self.__tela_venda.pega_dados_venda()          
            
        s = self.pega_venda_por_codigo(dados_venda["codigo_venda"])
        if s is None:
            venda = Venda(dados_venda["cliente"], dados_venda["codigo_produto"], dados_venda["quantidade"], dados_venda["codigo_venda"], dados_venda["data"])
            self.__vendas.append(venda)            
        else:
            self.__tela_venda.mostra_mensagem("ATENÇÃO: Venda já registrada")

    def remover_produto(self, venda: Venda):
        self.lista_venda()
        codigo_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_por_codigo_venda(codigo_venda)
        if venda is not None:
            codigo_produto = self.__tela_venda.seleciona_produto()  
            for produto in venda.produtos:
                if produto.codigo_produto == codigo_produto:
                    venda.produtos.remove(produto)
                    self.__tela_venda.mostra_mensagem("Produto removido com sucesso.")
                    return
            self.__tela_venda.mostra_mensagem("Produto não encontrado.")
        else:
            self.__tela_venda.mostra_mensagem("Venda não encontrada.")     

    

# Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_venda(self):
        for venda in self.__vendas:            
            self.__tela_venda.mostra_venda({"cliente": venda.cliente, "data": venda.data, "codigo": venda.codigo, "produtos": venda.produtos}) 
                    
    def excluir_venda(self):
        self.lista_venda()
        codigo_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_por_codigo_venda(codigo_venda)    

        if(venda is not None):
            self.__vendas.remove(venda)
            self.lista_venda()
        else:
            self.__tela_cliente.mostra_mensagem("ATENCÃO: Venda não existente")      

   
    def lista_produto(self):
    
        if not self.__produtos:
            self.__tela_venda.mostra_mensagem("Não há produtos adicionados nessa venda.")
            return
        
        for venda in self.__vendas:
            if venda.produtos:
                print(f"Código produto: {venda.codigo} (Quantidade: {venda.quantidade})")  
                for produto in venda.produtos:                    
                    self.__tela_cliente.mostra_produto(produto)
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_produto, 2: self.remover_produto, 3: self.lista_produto, 4: self.lista_venda, 5: self.finalizar_venda, 6: self.excluir_venda, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()   



    