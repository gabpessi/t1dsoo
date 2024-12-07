from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaCliente(AbstractTela):  
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
    if values['6']:
      opcao = 6
    if values['7']:
      opcao = 7
    if values['8']:
      opcao = 8
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao

  def init_opcoes(self):
      sg.ChangeLookAndFeel('BluePurple')
      layout = [
        [sg.Text('Clientes', font=("Helvica", 20, 'bold'), text_color='#00163A')],
        [sg.Text('Escolha sua opção', font=("Helvica", 15), text_color='#00163A')],
        [sg.Radio('Incluir Cliente', "RD1", key='1', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Alterar Cliente', "RD1", key='2', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Listar Clientes', "RD1", key='3', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Excluir Cliente', "RD1", key='4', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Incluir Animal', "RD1", key='5', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Alterar Animal', "RD1", key='6', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Excluir Animal', "RD1", key='7', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Listar Animais', "RD1", key='8', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Retornar', "RD1", key='0', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Clientes').Layout(layout)

  def pega_dados_cliente(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
        [sg.Text('Dados Cliente', font=('Helvetica', 15, 'bold'), 
             text_color='#00163A')],
        [sg.Text('Nome:', size=(10, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='nome')],
        [sg.Text('Telefone:', size=(10, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='telefone')],
        [sg.Text('Email:', size=(10, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='email')],
        [sg.Text('CPF:', size=(10, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='cpf')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
    ]
    self.__window = sg.Window('Sistema de Clientes', layout)

    while True:
        button, values = self.open()
        if button == 'Cancelar' or button is None:
            self.close()
            return None

        nome = values['nome']
        telefone = values['telefone']
        email = values['email']
        cpf = values['cpf']

        try:
          self.validar_tamanho(nome, 'Nome', min_tamanho=2)
          self.validar_tamanho(telefone, 'Telefone', min_tamanho=9)
          self.validar_apenas_letras(nome, 'Nome')
          self.validar_apenas_digitos(telefone, 'Telefone')
          self.validar_tamanho(email, 'Email', min_tamanho=5)
          self.validar_tamanho(cpf, 'CPF', min_tamanho=11, max_tamanho=11)
          self.validar_apenas_digitos(cpf, 'CPF')

          self.close()
          return {"nome": nome, "telefone": telefone, "email": email, "cpf": cpf}

        except Exception as e:
          self.mostra_mensagem(e)
 
  def mostra_cliente(self, dados_cliente):
    tabela_clientes = []
    for cliente in dados_cliente:
        if "animais" in cliente and cliente["animais"]:
            animais_cliente = "\n".join([f"{animal.nome_animal} (Cadastro: {animal.numero_cadastro})" for animal in cliente["animais"]])
        else:
            animais_cliente = "Nenhum animal cadastrado"

        tabela_clientes.append([
            cliente["nome"],
            cliente["telefone"],
            cliente["email"],
            cliente["cpf"],
            animais_cliente
        ])

    colunas = ["Nome", "Telefone", "E-mail", "CPF", "Animais"]

    layout = [
        [sg.Text("Lista de Clientes", font=("Helvica", 20, 'bold'),  text_color='#00163A')],
        [sg.Table(values=tabela_clientes,
                  headings=colunas,
                  auto_size_columns=True,
                  justification='center',
                  text_color='#00163A',
                  col_widths=[20, 15, 25, 15, 30],
                  row_height=30,
                  display_row_numbers=False,
                  key='-TABELA-',
                  enable_events=False)], 
        [sg.Button('OK')]
    ]

    self.__window = sg.Window("Lista de Clientes", layout, finalize=True)

    while True:
        event, values = self.__window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            self.__window.close()
            break

  def seleciona_cliente(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
      [sg.Text('Selecionar Cliente', font=("Helvica", 15, 'bold'), text_color='#00163A')],
      [sg.Text('Digite o CPF do cliente que deseja selecionar:', font=("Helvica", 11), text_color='#00163A')],
      [sg.Text('CPF:', size=(5, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='cpf')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona cliente').Layout(layout)

    while True:

      button, values = self.open()
      if button == 'Cancelar' or button is None:
          self.close()
          return None  
      
      cpf = values['cpf']

      try:
        self.validar_apenas_digitos(cpf, 'CPF')
        self.close()
        return cpf
      except Exception as e:
        self.mostra_mensagem(e)

  def seleciona_animal(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
      [sg.Text('Selecionar Animal', font=("Helvica", 15, 'bold'), text_color='#00163A')],
      [sg.Text('Digite o número de cadastro do animal que deseja selecionar:', font=("Helvica", 11),text_color='#00163A')],
      [sg.Text('Número de cadastro:', size=(15, 1), font=("Helvica", 11), text_color='#00163A'), sg.InputText('', key='numero_cadastro')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona animal').Layout(layout)

    while True:

      button, values = self.open()
      if button == 'Cancelar' or button is None:
          self.close()
          return None  
      
      numero_cadastro = values['numero_cadastro']

      try:
        self.validar_apenas_digitos(numero_cadastro, 'Número de Cadastro')
        self.close()
        return numero_cadastro
      except Exception as e:
        self.mostra_mensagem(e)
  
  def pega_dados_animal(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
        [sg.Text('Dados Animal', font=('Helvetica', 15, 'bold'), text_color='#00163A')],
        [sg.Text('Nome do Animal:', size=(16, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='nome_animal')],
        [sg.Text('Número de Cadastro:', size=(16, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='numero_cadastro')],
        [sg.Text('Idade:', size=(16, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='idade')],
        [sg.Text('Espécie:', size=(16, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='especie')],
        [sg.Text('Raça:', size=(16, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='raca')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de Animais', layout)

    while True:
        button, values = self.open()
        if button == 'Cancelar' or button is None:
            self.close()
            return None

        nome_animal = values['nome_animal']
        numero_cadastro = values['numero_cadastro']
        idade = values['idade']
        especie = values['especie']
        raca = values['raca']

        try:
            self.validar_tamanho(nome_animal, 'Nome do Animal', min_tamanho=2)
            self.validar_tamanho(numero_cadastro, 'Número de Cadastro', min_tamanho=1) 
            self.validar_tamanho(idade, 'Idade', min_tamanho=1)
            self.validar_tamanho(especie, 'Espécie', min_tamanho=2)
            self.validar_tamanho(raca, 'Raça', min_tamanho=2)

            self.close()
            return {
                "nome_animal": nome_animal,
                "numero_cadastro": numero_cadastro,
                "idade": int(idade),
                "especie": especie,
                "raca": raca
            }

        except Exception as e:
            self.mostra_mensagem(e)


  def mostra_animal(self, dados_animais):
    tabela_animais = []
    for animal, cpf_responsavel in dados_animais:
        tabela_animais.append([
            animal.nome_animal,
            animal.especie,
            animal.raca,
            animal.idade,
            animal.numero_cadastro,
            cpf_responsavel
        ])

    colunas = ["Nome do Animal", "Espécie", "Raça", "Idade", "Número de Cadastro", "CPF do Responsável"]

    layout = [
        [sg.Text("Lista de Animais", font=("Arial", 20, 'bold'), text_color='#00163A')],
        [sg.Table(values=tabela_animais,
                  headings=colunas,
                  text_color='#00163A',
                  auto_size_columns=True,
                  justification='center',
                  col_widths=[25, 15, 15, 10, 20, 15],
                  row_height=30,
                  display_row_numbers=False,
                  key='-TABELA-',
                  enable_events=False)],
        [sg.Button('OK')]
    ]

    self.__window = sg.Window("Lista de Animais", layout, finalize=True)

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