from limite.abstract_tela import AbstractTela
from datetime import datetime
import PySimpleGUI as sg

class TelaVeterinario(AbstractTela):  
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
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao

  def init_opcoes(self):
      sg.ChangeLookAndFeel('BluePurple')
      layout = [
        [sg.Text('Veterinários', font=("Helvica", 20, 'bold'), text_color='#00163A')],
        [sg.Text('Escolha sua opção', font=("Helvica", 15), text_color='#00163A')],
        [sg.Radio('Incluir Veterinário', "RD1", key='1', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Alterar Veterinário', "RD1", key='2', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Listar Veterinários', "RD1", key='3', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Excluir Veterinário', "RD1", key='4', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Adicionar Consulta', "RD1", key='5', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Remover Consulta', "RD1", key='6', font=('Helvetica', 11), text_color='#00163A')],        
        [sg.Radio('Listar Consulta', "RD1", key='7', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Radio('Retornar', "RD1", key='0', font=('Helvetica', 11), text_color='#00163A')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Veterinários').Layout(layout)
      
  def pega_dados_veterinario(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
        [sg.Text('DADOS VETERINÁRIO', font=("Times", 20))],
        [sg.Text('Nome:', size=(10, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='nome')],
        [sg.Text('Telefone:', size=(10, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='telefone')],
        [sg.Text('Email:', size=(10, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='email')],
        [sg.Text('CPF:', size=(10, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='cpf')],
        [sg.Text('Especialidade:', size=(10, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='especialidade')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
    ]
    self.__window = sg.Window('Sistema de Veterinários', layout)

    while True:
        button, values = self.open()
        if button == 'Cancelar' or button is None:
            self.close()
            return None

        nome = values['nome']
        telefone = values['telefone']
        email = values['email']
        cpf = values['cpf']
        especialidade = values['especialidade']

        try:
          self.validar_tamanho(nome, 'Nome', min_tamanho=2)
          self.validar_tamanho(telefone, 'Telefone', min_tamanho=9)
          self.validar_apenas_letras(nome, 'Nome')
          self.validar_apenas_digitos(telefone, 'Telefone')
          self.validar_tamanho(email, 'Email', min_tamanho=5)
          self.validar_tamanho(cpf, 'CPF', min_tamanho=11, max_tamanho=11)
          self.validar_apenas_digitos(cpf, 'CPF')
          self.validar_tamanho(especialidade, 'Especialidade', min_tamanho= 2)

          self.close()
          return {"nome": nome, "telefone": telefone, "email": email, "cpf": cpf, "especialidade": especialidade}

        except Exception as e:
          self.mostra_mensagem(e)
 
  def pega_codigo_consulta(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
      [sg.Text('Selecionar Consulta', font=("Helvica", 15, 'bold'), text_color='#00163A')],
      [sg.Text('Digite o código da consulta que deseja selecionar:', font=("Helvica", 11),text_color='#00163A')],
      [sg.Text('Código:', size=(10, 1), font=("Helvica", 11),text_color='#00163A'), sg.InputText('', key='codigo')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona consulta').Layout(layout)

    while True:

      button, values = self.open()
      if button == 'Cancelar' or button is None:
          self.close()
          return None  
      
      codigo = values['codigo']

      try:
        self.validar_apenas_digitos(codigo, 'Código da Consulta')
        self.close()
        return codigo
      except Exception as e:
        self.mostra_mensagem(e)
  

  def mostra_veterinario(self, dados_veterinario):
    tabela_veterinarios = []

    for veterinario in dados_veterinario:
        tabela_veterinarios.append([
            veterinario["nome"],
            veterinario["telefone"],
            veterinario["email"],
            veterinario["cpf"],
            veterinario["especialidade"]
        ])

    colunas = ["Nome", "Telefone", "E-mail", "CPF", "Especialidade"]

    layout = [
        [sg.Text("Lista de Veterinários", font=("Helvica", 20, 'bold'),  text_color='#00163A')],
        [sg.Table(values=tabela_veterinarios,
                  headings=colunas,
                  text_color='#00163A',
                  auto_size_columns=True,
                  justification='center',
                  col_widths=[20, 15, 25, 15, 20],
                  row_height=30,
                  display_row_numbers=False,
                  key='-TABELA-',
                  enable_events=False)],
        [sg.Button('OK')]
    ]

    self.__window = sg.Window("Lista de Veterinários", layout, finalize=True)

    while True:
        event, values = self.__window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            self.__window.close()
            break

  def mostra_consulta(self, dados_consultas, cpf_responsavel):
    tabela_consultas = []
    for consulta in dados_consultas:
        tabela_consultas.append([
            consulta.data.strftime('%d/%m/%Y'),
            consulta.horario,
            consulta.descricao,
            consulta.animal.nome_animal,
            consulta.servico.nome,
            consulta.codigo,
            cpf_responsavel
        ])

    colunas = ["Data", "Horário", "Descrição", "Animal", "Serviço", "Código", "CPF do Veterinário"]

    layout = [
        [sg.Text("Lista de Consultas", font=("Arial", 20))],
        [sg.Table(values=tabela_consultas,
                  headings=colunas,
                  auto_size_columns=True,
                  justification='center',
                  col_widths=[12, 8, 25, 15, 15, 10, 20],
                  row_height=30,
                  display_row_numbers=False,
                  key='-TABELA-',
                  enable_events=False)],
        [sg.Button('OK')]
    ]

    self.__window = sg.Window("Lista de Consultas", layout, finalize=True)

    while True:
        event, values = self.__window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            self.__window.close()
            break

  def seleciona_veterinario(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
      [sg.Text('Selecionar Veterinário', font=("Helvica", 15, 'bold'), text_color='#00163A')],
      [sg.Text('Digite o CPF do veterinario que deseja selecionar:', font=("Helvica", 11),text_color='#00163A')],
      [sg.Text('CPF:', size=(5, 1), font=("Helvica", 11),text_color='#00163A'), sg.InputText('', key='cpf')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Seleciona veterinário').Layout(layout)

    while True:

      button, values = self.open()
      if button == 'Cancelar' or button is None:
          self.close()
          return None  
      
      cpf = values['cpf']

      try:
        self.validar_apenas_digitos(cpf, 'CPF')
        self.validar_tamanho(cpf, 'CPF', min_tamanho=11, max_tamanho=11)       
        self.close()
        return cpf
      except Exception as e:
        self.mostra_mensagem(e)
  

  def mostra_mensagem(self, msg):
      sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values