from tela_sistema import TelaSistema
from controlador_servicos import ControladorServicos
from controlador_produtos import ControladorProdutos
from controlador_consultas import ControladorConsultas
from controlador_clientes import ControladorClientes
from controlador_veterinarios import ControladorVeterinarios
from controlador_vendas import ControladorVendas

class ControladorSistema:

    def __init__(self):
        self.__controlador_servicos = ControladorServicos(self)
        self.__controlador_produtos = ControladorProdutos(self)
        self.__controlador_consultas = ControladorConsultas(self)
        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_veterinarios = ControladorVeterinarios(self, self.__controlador_consultas)
        self.__controlador_vendas = ControladorVendas(self, self.__controlador_produtos, self.__controlador_clientes)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_servicos(self):
        return self.__controlador_servicos

    @property
    def controlador_produtos(self):
        return self.__controlador_produtos
    
    @property
    def controlador_consultas(self):
        return self.__controlador_consultas
    
    @property
    def controlador_clientes(self):
        return self.__controlador_clientes
    
    @property
    def controlador_veterinarios(self):
        return self.__controlador_veterinarios
    
    @property
    def controlador_vendas(self):
        return self.__controlador_vendas

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_servicos(self):              
        self.__controlador_servicos.abre_tela()

    def cadastra_produtos(self):              
        self.__controlador_produtos.abre_tela()
    
    def cadastra_consultas(self):
        self.__controlador_consultas.abre_tela()

    def cadastra_clientes(self):
        self.__controlador_clientes.abre_tela()
    
    def cadastra_veterinarios(self):
        self.__controlador_veterinarios.abre_tela()

    def cadastra_vendas(self):
        self.__controlador_vendas.abre_tela()

   
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_servicos, 2: self.cadastra_produtos, 3: self.cadastra_consultas, 4: self.cadastra_clientes, 5: self.cadastra_veterinarios, 6: self.cadastra_vendas}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()