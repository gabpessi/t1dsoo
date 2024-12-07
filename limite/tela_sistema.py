from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaSistema(AbstractTela):
   def __init__(self):
      self.__window = None
      self.init_components()
   
   def tela_opcoes(self):
      self.init_components()
      button, values = self.__window.Read()
      opcao = 0
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
      if values['0'] or button in (None,'Cancelar'):
            opcao = 0
      self.close()
      return opcao

   def close(self):
      self.__window.Close()
      
   def init_components(self):
      sg.ChangeLookAndFeel('BluePurple')
      layout = [
         [sg.Text('Bem vindo ao sistema de Petshop!', font=('Helvetica', 20, 'bold'), 
             text_color='#00163A')],
         [sg.Text('Escolha sua opção', font=('Helvetica', 15), 
             text_color='#00163A')],
         [sg.Radio('Serviços',"RD1", key='1', font=('Helvetica', 11), text_color='#00163A')],
         [sg.Radio('Produtos',"RD1", key='2', font=('Helvetica', 11), text_color='#00163A')],
         [sg.Radio('Clientes',"RD1", key='3', font=('Helvetica', 11), text_color='#00163A')],
         [sg.Radio('Consultas',"RD1", key='4', font=('Helvetica', 11), text_color='#00163A')],
         [sg.Radio('Veterinarios',"RD1", key='5', font=('Helvetica', 11), text_color='#00163A')],
         [sg.Radio('Vendas',"RD1", key='6', font=('Helvetica', 11), text_color='#00163A')],
         [sg.Radio('Finalizar sistema',"RD1", key='0', font=('Helvetica', 11), text_color='#00163A')],
         [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
      self.__window = sg.Window('Sistema do Petshop').Layout(layout)
      