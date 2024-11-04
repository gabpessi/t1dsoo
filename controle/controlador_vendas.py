from limite.tela_venda import TelaVenda
from entidade.venda import Venda
from exceptions.nenhuma_venda_ativa_exception import NenhumaVendaAtivaException
from exceptions.venda_em_andamento_exception import VendaEmAndamentoException
from exceptions.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exceptions.quantidade_insuficiente_exception import QuantidadeInsuficienteException
from exceptions.lista_vazia_exception import ListaVaziaException

class ControladorVendas:
    def __init__(self, controlador_sistema):        
        self.__vendas = []            
        self.__controlador_sistema = controlador_sistema
        self.__tela_venda = TelaVenda()            
        self.__venda_atual = None  

    def iniciar_venda(self):
        try:
            if self.__venda_atual:  
                raise VendaEmAndamentoException()
            cpf_cliente = self.__controlador_sistema.controlador_clientes.seleciona_cliente()
            cliente = self.__controlador_sistema.controlador_clientes.pega_cliente_por_cpf(cpf_cliente)
            
            if cliente:
                self.__venda_atual = Venda(cliente) 
                self.__tela_venda.mostra_mensagem(f"Nova venda iniciada para {cliente.nome}.")
            else:
                raise ObjetoNaoEncontradoException("Cliente")
            
        except VendaEmAndamentoException as e:
            self.__tela_venda.mostra_mensagem(e)
        except ObjetoNaoEncontradoException as e:
            self.__tela_venda.mostra_mensagem(e)

    def adicionar_produto(self):
        try:
            if not self.__venda_atual:
                raise NenhumaVendaAtivaException()
            codigo_produto = self.__controlador_sistema.controlador_produtos.seleciona_produto()
            produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(codigo_produto)

            if produto:
                quantidade = self.__tela_venda.pega_quantidade_produto()  
                if quantidade > produto.quantidade_estoque:
                    raise QuantidadeInsuficienteException()
                
                
                produto.atualizar_estoque(-quantidade)
                self.__venda_atual.produtos.append((produto, quantidade))
                self.__venda_atual.valor_total += produto.preco * quantidade
                
                self.listar_produtos_venda_atual()
                self.__tela_venda.mostra_mensagem("Produto adicionado com sucesso à venda atual.")
            else:
                raise ObjetoNaoEncontradoException("Produto")
            
        except NenhumaVendaAtivaException as e:
            self.__tela_venda.mostra_mensagem(e)
        except QuantidadeInsuficienteException as e:
            self.__tela_venda.mostra_mensagem(e)    
        except ObjetoNaoEncontradoException as e:
            self.__tela_venda.mostra_mensagem(e)         

    def remover_produto(self):
        try:
            if not self.__venda_atual:
                raise NenhumaVendaAtivaException()
            self.listar_produtos_venda_atual()
            codigo_produto = self.__controlador_sistema.controlador_produtos.seleciona_produto()
            produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(codigo_produto)

            if produto is not None:
                for p, q in self.__venda_atual.produtos:
                    if p == produto:
                        self.__venda_atual.produtos.remove((p, q))
                        self.__venda_atual.valor_total -= produto.preco * q
                        produto.atualizar_estoque(q)                
                        self.__tela_venda.mostra_mensagem("Produto removido da venda atual com sucesso.")
                        break
            else:
                raise ObjetoNaoEncontradoException("Produto")
            
        except NenhumaVendaAtivaException as e:
            self.__tela_venda.mostra_mensagem(e)           
        except ObjetoNaoEncontradoException as e:
            self.__tela_venda.mostra_mensagem(e)         

    def listar_produtos_venda_atual(self):
        try:
            if not self.__venda_atual:
                raise NenhumaVendaAtivaException()

            if not self.__venda_atual.produtos:
                raise ListaVaziaException("produtos da venda atual")
            
            for produto, quantidade in self.__venda_atual.produtos:
                self.__tela_venda.mostra_produto_venda(produto.nome, quantidade)
        
        except NenhumaVendaAtivaException as e:
            self.__tela_venda.mostra_mensagem(e)
        except ListaVaziaException as e:
            self.__tela_venda.mostra_mensagem(e)

    def finalizar_venda(self):
        try:
            if not self.__venda_atual:
                raise NenhumaVendaAtivaException()
                
            if not self.__venda_atual.produtos:
                raise ListaVaziaException("produtos da venda")
            
            mensagem = f'Venda finalizada para {self.__venda_atual.cliente.nome}. Valor total: R${self.__venda_atual.valor_total:.2f}'
            self.__vendas.append(self.__venda_atual)
            self.__tela_venda.mostra_mensagem(mensagem)
            self.__venda_atual = None

        except NenhumaVendaAtivaException as e:
            self.__tela_venda.mostra_mensagem(e)           
        except ListaVaziaException as e:
            self.__tela_venda.mostra_mensagem(e)     

    def lista_venda(self):
        try:
            if not self.__vendas:
                raise ListaVaziaException("vendas") 
            for venda in self.__vendas:                       
                self.__tela_venda.mostra_venda(venda)

        except ListaVaziaException as e:
            self.__tela_venda.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.iniciar_venda, 
            2: self.adicionar_produto, 
            3: self.remover_produto,
            4: self.listar_produtos_venda_atual, 
            5: self.lista_venda, 
            6: self.finalizar_venda, 
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_venda.tela_opcoes()]()
