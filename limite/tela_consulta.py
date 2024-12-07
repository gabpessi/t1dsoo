from limite.abstract_tela import AbstractTela
from datetime import datetime
import PySimpleGUI as sg 

class TelaConsulta(AbstractTela):  
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
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao
  
  def init_opcoes(self):    
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
      [sg.Text('Consultas', font=("Helvica", 20, 'bold'), text_color='#00163A')],
      [sg.Text('Escolha sua opção', font=("Helvica", 15), text_color='#00163A')],
      [sg.Radio('Incluir Consulta', "RD1", key='1', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Alterar Consulta', "RD1", key='2', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Listar Consultas', "RD1", key='3', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Excluir Consulta', "RD1", key='4', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Exibir Detalhes', "RD1", key='5', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Gerar Relatório', "RD1", key='6', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Radio('Retornar', "RD1", key='0', font=('Helvetica', 11), text_color='#00163A')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema do Petshop').Layout(layout)


  def pega_dados_consulta(self):
      sg.ChangeLookAndFeel('BluePurple')
      layout = [
        [sg.Text('Dados Consulta',font=('Helvetica', 15, 'bold'), 
             text_color='#00163A')],
        [sg.Text('Data:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='data')],
        [sg.Text('Horário:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='horario')],
        [sg.Text('Descricão:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='descricao')],
        [sg.Text('Código do Animal:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='codigo_animal')],
        [sg.Text('Código do Serviço:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='codigo_servico')],
        [sg.Text('Código da Consulta:', size=(15, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='codigo')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
      ]
      self.__window = sg.Window('Sistema de consultas').Layout(layout)

      while True:
        
        button, values = self.open()
        if button == 'Cancelar' or button is None:
          self.close()
          return None        

        data = values['data']
        horario = values['horario']
        descricao = values['descricao'] 
        codigo_animal = values['codigo_animal'] 
        codigo_servico = values['codigo_servico'] 
        codigo = values['codigo'] 

        try:
          data_obj = self.le_data(data, 'Data')
          horario_obj = self.le_horario(horario, 'Horário')
          self.validar_apenas_letras(descricao, 'Descricao')
          self.validar_apenas_digitos(codigo_animal, 'Código do Animal')
          self.validar_apenas_digitos(codigo_servico, 'Código do Serviço')
          self.validar_apenas_digitos(codigo_animal, 'Código do Animal')          
          self.validar_apenas_digitos(codigo, 'Código da Consulta')
          self.__window.close()
          return {
            "data": data_obj,
            "horario": horario_obj,
            "descricao": descricao,
            "codigo_animal": codigo_animal,
            "codigo_servico": codigo_servico,
            "codigo": codigo
          }
        
        except Exception as e:
          self.mostra_mensagem(e)
          
      
  def mostra_consulta(self, dados_consulta):     
    tabela_consultas = []
    for dado in dados_consulta:
        tabela_consultas.append([
            dado["data"].strftime('%d/%m/%Y'),  
            dado["horario"],                    
            dado["descricao"],                  
            dado["animal"].nome_animal,         
            dado["animal"].numero_cadastro,     
            dado["servico"].nome,               
            dado["servico"].codigo,             
            dado["codigo"]                     
        ])

    colunas = ["Data", "Horário", "Descrição", "Animal", "Número Cadastro", "Serviço", "Código Serviço", "Código Consulta"]

    layout = [
        [sg.Text("Lista de Consultas", font=("Helvica", 20, 'bold'),  text_color='#00163A')],
        [sg.Table(values=tabela_consultas,
                  headings=colunas,
                  auto_size_columns=True,
                  text_color='#00163A',
                  justification='center',
                  col_widths=[15, 15, 30, 20, 20, 20, 15, 15],
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

  def mostra_relatorio(self, mes, especie, raca, servico):
    tabela_relatorio = [
        ["Mês com mais consultas", mes],
        ["Espécie que mais fez consultas", especie],
        ["Raça que mais fez consultas", raca],
        ["Serviço mais realizado", servico]
    ]

    colunas = ["Descrição", "Valor"]

    layout = [
        [sg.Text("Relatório de Consultas", font=("Helvica", 20, 'bold'),  text_color='#00163A')],
        [sg.Table(values=tabela_relatorio,
                  headings=colunas,
                  text_color='#00163A',
                  auto_size_columns=True,
                  justification='center',
                  col_widths=[40, 40],
                  row_height=30,
                  display_row_numbers=False,
                  key='-TABELA-',
                  enable_events=False)],
        [sg.Button('OK')]
    ]

    self.__window = sg.Window("Relatório de Consultas", layout, finalize=True)

    while True:
        event, values = self.__window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            self.__window.close()
            break

  def seleciona_consulta(self):
    sg.ChangeLookAndFeel('BluePurple')
    layout = [
      [sg.Text('Selecionar Consulta', font=("Helvica", 15, 'bold'), text_color='#00163A')],
      [sg.Text('Digite o código da consulta que deseja selecionar:', font=("Helvica", 11), text_color='#00163A')],
      [sg.Text('Código:', size=(5, 1), font=('Helvetica', 11), text_color='#00163A'), sg.InputText('', key='codigo')],
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
  

  def solicita_periodo(self):
        sg.ChangeLookAndFeel('BluePurple')

        layout = [
            [sg.Text('Selecionar período para o relatório', font=("Helvica", 15, 'bold'), text_color='#00163A')],
            [sg.Text('Digite o período desejado para o relatório:', font=("Helvica", 11), text_color='#00163A')],
            [sg.Text('Data Inicial (DD/MM/AAAA):', size=(20, 1)), sg.InputText('', key='data_inicio', font=("Helvica", 11), text_color='#00163A')],
            [sg.Text('Data Final (DD/MM/AAAA):', size=(20, 1)), sg.InputText('', key='data_fim', font=("Helvica", 11), text_color='#00163A')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        
        self.__window = sg.Window('Seleciona Período', layout, finalize=True)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                self.__window.close()
                return None

            data_inicio = values['data_inicio']
            data_fim = values['data_fim']

            try:
                data_inicio = self.le_data(data_inicio, 'Data Inicial')
                data_fim = self.le_data(data_fim, 'Data Final')

                self.__window.close()
                return data_inicio, data_fim

            except ValueError as e:
                self.mostra_mensagem(e)
                continue
 
  def mostra_mensagem(self, msg):
      sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values