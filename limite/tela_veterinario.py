from limite.abstract_tela import AbstractTela
from datetime import datetime

class TelaVeterinario(AbstractTela):  
  def __init__(self) -> None:
        pass

  def tela_opcoes(self):
    print("-------- VETERINARIOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Veterinário")
    print("2 - Alterar Veterinário")
    print("3 - Listar Veterinário")
    print("4 - Excluir Veterinário")   
    print("5 - Adicionar Consulta") 
    print("6 - Remover Consulta") 
    print("7 - Listar Consulta")    
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha a opcao: ", [1,2,3,4,5,6,7,0])
    return opcao

  
  def pega_dados_veterinario(self):
    print("-------- DADOS VETERINARIO ----------")
    nome = self.le_string_com_tamanho("Nome: ", min_tamanho=2, campo="nome", somente_letras=True)
    telefone = self.le_string_com_tamanho("Telefone: ", min_tamanho=9, campo="telefone", somente_digitos=True)
    email = self.le_email("Email: ")
    cpf = self.le_string_com_tamanho("CPF: ", min_tamanho=11, max_tamanho=11, campo="CPF", somente_digitos=True)
    especialidade = self.le_string_com_tamanho("Especialidade: ", min_tamanho=2, campo="especialidade", somente_letras=True)

    return {"nome": nome, "telefone": telefone, "email": email, "cpf": cpf, "especialidade": especialidade}

  def pega_codigo_consulta(self):
    codigo = self.le_string_com_tamanho("Código da Consulta: ", campo="Código da Consulta", somente_digitos=True)
    return codigo      
  
  def mostra_consulta(self, dados_consulta):
    
    for consulta in dados_consulta:                
        print("DATA DA CONSULTA: ", consulta.data.strftime('%d/%m/%Y'))
        print("HORARIO DA CONSULTA: ", consulta.horario)
        print("DESCRICAO DA CONSULTA: ", consulta.descricao)
        print("ANIMAL DA CONSULTA: ", consulta.animal.nome_animal)
        print("SERVICO DA CONSULTA: ", consulta.servico.nome)
        print("CODIGO DA CONSULTA: ", consulta.codigo)
        print("\n")


  def mostra_veterinario(self, dados_veterinario):
    print("NOME DO VETERINARIO: ", dados_veterinario["nome"])
    print("TELEFONE DO VETERINARIO: ", dados_veterinario["telefone"])
    print("EMAIL DO VETERINARIO: ", dados_veterinario["email"])
    print("CPF DO VETERINARIO: ", dados_veterinario["cpf"])  
    print("ESPECIALIDADE DO VETERINARIO", dados_veterinario["especialidade"])
    
    if "consultas" in dados_veterinario and dados_veterinario["consultas"]:
        print("CONSULTAS DO VETERINARIO: ")
        
        for consulta in dados_veterinario["consultas"]:            
            print(f"Data: {consulta.data}, código da consulta: {consulta.codigo}")
          
    else:
        print("Este veterinário não possui consultas cadastradas.")

    print("\n")


  def seleciona_veterinario(self):
    cpf = self.le_string_com_tamanho("CPF do Veterinario: ", min_tamanho=11, max_tamanho=11, campo="CPF", somente_digitos=True)
    return cpf
  

  def mostra_mensagem(self, msg):
    print(msg)