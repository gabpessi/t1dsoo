from limite.tela_venda import TelaVenda
from entidade.venda import Venda
from exceptions.nenhuma_venda_ativa_exception import NenhumaVendaAtivaException
from exceptions.venda_em_andamento_exception import VendaEmAndamentoException
from DAOs.venda_dao import VendaDAO
from exceptions.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exceptions.quantidade_insuficiente_exception import QuantidadeInsuficienteException
from exceptions.lista_vazia_exception import ListaVaziaException

class ControladorVendas:
    def __init__(self, controlador_sistema):        
        self.__venda_DAO = VendaDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_venda = TelaVenda()            
        self.__venda_atual = None  

    def iniciar_venda(self):
        try:
            if self.__venda_atual:  
                raise VendaEmAndamentoException()
            self.__controlador_sistema.controlador_clientes.lista_cliente() 
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
            
            self.__controlador_sistema.controlador_produtos.lista_produto()
            codigo_produto = self.__controlador_sistema.controlador_produtos.seleciona_produto()
            produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(codigo_produto)

            if produto:
                quantidade = self.__tela_venda.pega_quantidade_produto()
                quantidade_estoque = int(produto.quantidade_estoque)
            
                if quantidade > quantidade_estoque:
                    raise QuantidadeInsuficienteException()
                
                produto.atualizar_estoque(-quantidade)
                self.__controlador_sistema.controlador_produtos.get_produto_DAO().update(produto)                
                self.__venda_atual.produtos.append((produto, quantidade))                
                preco_produto = float(produto.preco)
                self.__venda_atual.valor_total += preco_produto * quantidade
                
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
        except ValueError:
            self.__tela_venda.mostra_mensagem("Erro ao converter valores. Certifique-se de inserir números válidos.")
  
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
                        produto.atualizar_estoque(q)
                        self.__controlador_sistema.controlador_produtos.get_produto_DAO().update(produto)
                        self.__venda_atual.produtos.remove((p, q))
                        preco_produto = float(produto.preco)
                        self.__venda_atual.valor_total -= preco_produto * q
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
            self.__tela_venda.mostra_produtos_venda(self.__venda_atual.produtos)

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
            self.__venda_DAO.add(self.__venda_atual)
            self.__tela_venda.mostra_mensagem(mensagem)
            self.__venda_atual = None

        except NenhumaVendaAtivaException as e:
            self.__tela_venda.mostra_mensagem(e)           
        except ListaVaziaException as e:
            self.__tela_venda.mostra_mensagem(e)    

    def lista_venda(self):
        dados_vendas = []
        try:
            if not self.__venda_DAO.get_all():
                raise ListaVaziaException("vendas") 
            for venda in self.__venda_DAO.get_all():  
                dados_vendas.append(venda)                     
            self.__tela_venda.mostra_venda(dados_vendas)

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
