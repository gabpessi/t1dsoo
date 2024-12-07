from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg 

class TelaProduto(AbstractTela):
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
    if values['5']:
      opcao = 5      
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao
    
  def init_opcoes(self):    
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
      [sg.Text('Produtos', font=("Helvica", 20, 'bold'), text_color='#00163A')],
      [sg.Text('Escolha sua opção', font=("Helvica", 15), text_color='#00163A')],
      [sg.Radio('Incluir Produto', "RD1", key='1', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Alterar Produto', "RD1", key='2', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Listar Produtos', "RD1", key='3', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Excluir Produto', "RD1", key='4', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Verificar Disponibilidade', "RD1", key='5', font=('Helvetica', 11), text_color='#00163A')],      
      [sg.Radio('Retornar', "RD1", key='0', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Produtos').Layout(layout)

  def pega_dados_produto(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
        [sg.Text('Dados Produto', font=('Helvetica', 15, 'bold'), 
             text_color='#00163A')],
        [sg.Text('Nome:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='nome')],
        [sg.Text('Preço:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='preco')],
        [sg.Text('Código do Produto:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='codigo')],
        [sg.Text('Quantidade Estoque:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='quantidade_estoque')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
    ]
    self.__window = sg.Window('Sistema de produtos').Layout(layout)

    while True:
        button, values = self.open()
        if button == 'Cancelar' or button is None:
            self.close()
            return None        

        nome = values['nome']
        preco = values['preco']
        codigo = values['codigo'] 
        quantidade_estoque = values['quantidade_estoque']
        
        try:
            self.validar_tamanho(nome, 'Nome', min_tamanho=2)
            self.validar_tamanho(preco, 'Preço', min_tamanho=1)
            self.validar_apenas_letras(nome, 'Nome')
            self.validar_apenas_digitos(codigo, 'Código do Produto')
            self.validar_apenas_digitos(quantidade_estoque, 'Quantidade no Estoque')

            preco = float(preco)
            quantidade_estoque = int(quantidade_estoque)            

        except Exception as e:
            print(e)
            self.mostra_mensagem(e)
            self.__window.close()
            return None

        self.close() 
        return {"nome": nome, "preco": preco, "codigo": codigo, "quantidade_estoque": quantidade_estoque}
  
  def mostra_produto(self, dados_produto):
    
    tabela_produtos = []
    for dado in dados_produto:
        tabela_produtos.append([
            dado["nome"],
            f"R$ {dado['preco']}",
            dado["codigo"],
            dado["quantidade_estoque"]
        ])

    colunas = ["Nome", "Preço", "Código", "Quantidade em Estoque"]

    layout = [
        [sg.Text("Lista de Produtos", font=("Helvica", 20, 'bold'),  text_color='#00163A')],
        [sg.Table(values=tabela_produtos,
                  headings=colunas,
                  auto_size_columns=True,
                  text_color='#00163A',
                  justification='center',
                  col_widths=[20, 10, 10, 15],
                  row_height=30,
                  display_row_numbers=False,
                  key='-TABELA-',
                  enable_events=False)],
        [sg.Button('OK')]
    ]

    self.__window = sg.Window("Lista de Produtos", layout, finalize=True)

    while True:
        event, values = self.__window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            self.__window.close()
            break

  
  def seleciona_produto(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
      [sg.Text('Selecionar Serviço', font=("Helvica", 15, 'bold'), text_color='#00163A')],
      [sg.Text('Digite o código do produto que deseja selecionar:', font=("Helvica", 11), text_color='#00163A')],
      [sg.Text('Código:', size=(6, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='codigo')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona produto').Layout(layout)

    while True:
      button, values = self.open()
      if button == 'Cancelar' or button is None:
          self.close()
          return None  
      
      codigo = values['codigo']

      try:
        self.validar_apenas_digitos(codigo, 'Código do Produto')
        self.close()
        return codigo
      except Exception as e:
        self.mostra_mensagem(e)
  

  def mostra_mensagem(self, msg):
      sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values