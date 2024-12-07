import uuid
from datetime import datetime
from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaVenda(AbstractTela): 
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6       
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao    

    def init_opcoes(self):
        sg.ChangeLookAndFeel('BluePurple')
        layout = [
        [sg.Text('Vendas', font=("Helvica", 20, 'bold'), text_color='#00163A')],
        [sg.Text('Escolha sua opção', font=("Helvica", 15), text_color='#00163A')],
        [sg.Radio('Iniciar Venda', "RD1", key='1', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Adicionar Produto', "RD1", key='2', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Remover Produto', "RD1", key='3', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Listar Produtos da Venda Atual', "RD1", key='4', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Listar Vendas', "RD1", key='5', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Finalizar Venda', "RD1", key='6', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Retornar', "RD1", key='0', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Vendas').Layout(layout)
    
    def pega_quantidade_produto(self):
        sg.ChangeLookAndFeel('BluePurple')
        layout = [
            [sg.Text('Selecionar Quantidade', font=("Helvica", 15, 'bold'), text_color='#00163A')],
            [sg.Text('Digite a quantidade do produto:', font=("Helvica", 11), text_color='#00163A')],
            [sg.Text('Quantidade:', size=(10, 1), font=("Helvica", 11), text_color='#00163A'), sg.InputText('', key='quantidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona quantidade').Layout(layout)

        button, values = self.open()
        
        try:
            quantidade = int(values['quantidade']) 
        except ValueError:
            self.mostra_mensagem("Quantidade inválida. Digite um número válido.")
            self.close()
            return None

        self.close()
        return quantidade

    def seleciona_produto(self):
        sg.ChangeLookAndFeel('BluePurple')
        layout = [
        [sg.Text('Selecionar Produto', font=("Helvica", 15, 'bold'), text_color='#00163A')],
        [sg.Text('Digite o código do produto:', font=("Helvica", 11), text_color='#00163A')],
        [sg.Text('Código:', size=(15, 1), font=("Helvica", 11), text_color='#00163A'), sg.InputText('', key='codigo')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona produto').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo            
    
    def mostra_venda(self, vendas):
        if not vendas:
            sg.Popup("Nenhuma venda encontrada.", title="Erro")
            return

        tabela_vendas = []
        for venda in vendas:
            produtos_texto = ""
            if venda.produtos:
                produtos_texto = ", ".join(
                    [f"{produto.nome} (Qtd: {quantidade})" for produto, quantidade in venda.produtos]
                )
            else:
                produtos_texto = "Nenhum produto"

            tabela_vendas.append([
                venda.cliente.nome,
                venda.cliente.cpf,
                venda.data.strftime('%d/%m/%Y'),
                venda.codigo_venda,
                produtos_texto,
                f"R$ {venda.valor_total:.2f}"
            ])

        colunas = ["Cliente", "CPF", "Data", "Código da Venda", "Produtos", "Valor Total"]

        layout = [
            [sg.Text("Lista de Vendas", font=("Helvica", 20, 'bold'),  text_color='#00163A')],
            [sg.Table(values=tabela_vendas,
                    headings=colunas,
                    auto_size_columns=True,
                    text_color='#00163A',
                    justification='center',
                    col_widths=[20, 15, 12, 15, 30, 12],
                    row_height=30,
                    display_row_numbers=False,
                    key='-TABELA-',
                    enable_events=False)],
            [sg.Button('OK')]
    ]

        self.__window = sg.Window("Lista de Vendas", layout, finalize=True)

        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED or event == 'OK':
                self.__window.close()
                break

    def mostra_produtos_venda(self, produtos):     
        
        tabela_produtos = [
            [produto.codigo, produto.nome, quantidade]
            for produto, quantidade in produtos
        ]

        colunas = ["Código", "Produto", "Quantidade"]

        layout = [
            [sg.Text("Produtos da Venda", font=("Helvica", 20, 'bold'),  text_color='#00163A')],
            [sg.Table(
                values=tabela_produtos,
                headings=colunas,
                text_color='#00163A',
                auto_size_columns=True,
                justification='center',
                col_widths=[12, 30, 10],
                row_height=30,
                display_row_numbers=False,
                key='-TABELA-',
                enable_events=False
            )],
            [sg.Button('OK')]
        ]

        self.__window = sg.Window("Lista de Produtos da Venda", layout, finalize=True)

        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED or event == 'OK':
                self.__window.close()
                break


    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values