from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg 

class TelaServico(AbstractTela):  
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
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao    

  def init_opcoes(self):    
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
      [sg.Text('Serviços', font=("Helvica", 20, 'bold'), text_color='#00163A')],
      [sg.Text('Escolha sua opção', font=("Helvica", 15), text_color='#00163A')],
      [sg.Radio('Incluir Serviço', "RD1", key='1', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Alterar Serviço', "RD1", key='2', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Listar Serviços', "RD1", key='3', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Excluir Serviço', "RD1", key='4', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Retornar', "RD1", key='0', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Serviços').Layout(layout)

  def pega_dados_servico(self):
      sg.ChangeLookAndFeel('BluePurple')
      layout = [
        [sg.Text('Dados Serviço', font=('Helvetica', 15, 'bold'), 
             text_color='#00163A')],
        [sg.Text('Nome:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='nome')],
        [sg.Text('Preco:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='preco')],
        [sg.Text('Código do Serviço:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='codigo')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
      ]
      self.__window = sg.Window('Sistema de serviços').Layout(layout)

      while True:
        
        button, values = self.open()
        if button == 'Cancelar' or button is None:
          self.close()
          return None        

        nome = values['nome']
        preco = values['preco']
        codigo = values['codigo'] 
        
        try:
          self.validar_tamanho(nome, 'Nome', min_tamanho=2)
          self.validar_tamanho(preco, 'Preço', min_tamanho=1)
          self.validar_apenas_letras(nome, 'Nome')
          self.validar_apenas_digitos(preco, 'Preço')
          self.validar_tamanho(codigo, 'Código do Serviço', min_tamanho=1, max_tamanho=10)
          self.validar_apenas_digitos(codigo, 'Código do Serviço')

          self.close() 
          return {"nome": nome, "preco": preco, "codigo": codigo}
        
        except Exception as e:
          self.mostra_mensagem(e)

  def mostra_servico(self, dados_servico):
    tabela_servicos = []
    for dado in dados_servico:
        tabela_servicos.append([dado["nome"], f"R$ {dado["preco"]}", dado["codigo"]])

    colunas = ["Nome", "Preço", "Código"]

    layout = [
        [sg.Text("Lista de Serviços", font=("Helvica", 20, 'bold'),  text_color='#00163A')],
        [sg.Table(values=tabela_servicos,
                  headings=colunas,
                  auto_size_columns=True,
                  text_color='#00163A',
                  justification='center',
                  col_widths=[20, 15, 10],
                  row_height=30,
                  display_row_numbers=False,
                  key='-TABELA-',
                  enable_events=False)],
        [sg.Button('OK')]
    ]

    self.__window = sg.Window("Lista de Serviços", layout, finalize=True)

    while True:
        event, values = self.__window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            self.__window.close()
            break

  def seleciona_servico(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
      [sg.Text('Selecionar Serviço', font=("Helvica", 15, 'bold'), text_color='#00163A')],
      [sg.Text('Digite o código do serviço que deseja selecionar:', font=("Helvica", 11), text_color='#00163A')],
      [sg.Text('Código:', size=(5, 1), font=('Helvetica', 11), text_color='#00163A'),  sg.InputText('', key='codigo')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona serviço').Layout(layout)

    while True:

      button, values = self.open()
      if button == 'Cancelar' or button is None:
          self.close()
          return None  
      
      codigo = values['codigo']

      try:
        self.validar_apenas_digitos(codigo, 'Código do Serviço')
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