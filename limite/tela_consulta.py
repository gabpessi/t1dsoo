from limite.abstract_tela import AbstractTela
from datetime import datetime

class TelaConsulta(AbstractTela):  
  def __init__(self) -> None:
        pass

  def tela_opcoes(self):
    print("-------- CONSULTAS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Consulta")
    print("2 - Alterar Consulta")
    print("3 - Listar Consulta")
    print("4 - Excluir Consulta")   
    print("5 - Exibir Detalhes")
    print("6 - Gerar Relatório") 
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,5,6,0])
    return opcao


  def pega_dados_consulta(self): 
      print("-------- DADOS CONSULTA ----------")
      data = self.le_data() 
      horario = self.le_horario() 
      descricao = input("Descrição: ")
      codigo_animal = self.le_string_com_tamanho("Número de Cadastro do Animal: ", campo="Número de Cadastro do Animal", somente_digitos=True)
      codigo_servico = self.le_string_com_tamanho("Código do Serviço: ", campo="Código do Serviço", somente_digitos=True)
      codigo = self.le_string_com_tamanho("Código da Consulta: ", campo="Código da Consulta", somente_digitos=True)
    

      return {
        "data": data,
        "horario": horario,
        "descricao": descricao,
        "codigo_animal": codigo_animal,
        "codigo_servico": codigo_servico,
        "codigo": codigo
       }

  def mostra_consulta(self, dados_consulta):    
    print("DATA DA CONSULTA: ", dados_consulta["data"].strftime('%d/%m/%Y'))
    print("HORARIO DA CONSULTA: ", dados_consulta["horario"])
    print("DESCRICAO DA CONSULTA: ", dados_consulta["descricao"])
    print("ANIMAL DA CONSULTA: ", dados_consulta["animal"].nome_animal)
    print("NÚMERO DE CADASTRO ANIMAL: ", dados_consulta["animal"].numero_cadastro)
    print("SERVICO DA CONSULTA: ", dados_consulta["servico"].nome)
    print( "CÓDIGO DO SERVIÇO: ", dados_consulta["servico"].codigo)
    print("CODIGO DA CONSULTA: ", dados_consulta["codigo"])    
    print("\n")    
    

  def mostra_relatorio(self, mes, especie, raca, servico):
    print("-------- RELATÓRIO ----------")
    print(f"Mês com mais consultas: {mes}")
    print(f"Espécie que mais fez consultas: {especie}")
    print(f"Raça que mais fez consultas: {raca}")
    print(f"Serviço mais realizado: {servico}")
    print("\n")


  def seleciona_consulta(self):
    codigo = self.le_string_com_tamanho("Código da Consulta: ", somente_digitos=True)
    return codigo
  

  def solicita_periodo(self):
        print("Informe o período para o relatório:")
        data_inicio = self.le_data("Data inicial (DD/MM/AAAA): ")
        data_fim = self.le_data("Data final (DD/MM/AAAA): ")
        return data_inicio, data_fim

  
  def mostra_relatorio(self, mes_mais_consultas, especie_mais_consultada, raca_mais_consultada, servico_mais_realizado):
        print("-------- RELATÓRIO ----------")
        print(f"Mês com mais consultas: {mes_mais_consultas}")
        print(f"Espécie que mais fez consultas: {especie_mais_consultada}")
        print(f"Raça que mais fez consultas: {raca_mais_consultada}")
        print(f"Serviço mais realizado: {servico_mais_realizado}")
        print("------------------------------")

  def mostra_mensagem(self, msg):
    print(msg)