from limite.tela_consulta import TelaConsulta
from entidade.consulta import Consulta
import locale
from DAOs.consulta_dao import ConsultaDAO
from exceptions.lista_vazia_exception import ListaVaziaException
from exceptions.objeto_nao_encontrado_exception import ObjetoNaoEncontradoException
from exceptions.objeto_repetido_exception import ObjetoRepetidoException

class ControladorConsultas():
    def __init__(self, controlador_sistema):        
        self.__consulta_DAO = ConsultaDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_consulta = TelaConsulta()

    def pega_consulta_por_codigo(self, codigo: int):
        for consulta in self.__consulta_DAO.get_all():
            if(consulta.codigo == codigo):
                return consulta
        return None
    
    def seleciona_consulta(self):
        return self.__tela_consulta.seleciona_consulta()

    def incluir_consulta(self):
        dados_consulta = self.__tela_consulta.pega_dados_consulta() 
        if not dados_consulta:
            return   
        try:
            animal = self.__controlador_sistema.controlador_clientes.pega_animal_por_numero_cadastro(dados_consulta["codigo_animal"])
            if animal is None:
                raise ObjetoNaoEncontradoException("Animal")           
            
            servico = self.__controlador_sistema.controlador_servicos.pega_servico_por_codigo(dados_consulta["codigo_servico"])
            if servico is None:            
                raise ObjetoNaoEncontradoException("Serviço")             
          
            consulta_existente = self.pega_consulta_por_codigo(dados_consulta["codigo"])
            if consulta_existente is not None:
                raise ObjetoRepetidoException("Consulta", dados_consulta["codigo"])
            
            consulta = Consulta(dados_consulta["data"], dados_consulta["horario"], dados_consulta["descricao"], animal, servico, dados_consulta["codigo"])
            self.__consulta_DAO.add(consulta)
            self.__tela_consulta.mostra_mensagem("Consulta cadastrada com sucesso!")
        
        except ObjetoNaoEncontradoException as e:
            self.__tela_consulta.mostra_mensagem(e)
        except ObjetoRepetidoException as e:
            self.__tela_consulta.mostra_mensagem(e)


    def alterar_consulta(self):
        try:
            if self.__consulta_DAO.get_all() == None: 
                raise ListaVaziaException("consultas")
            self.lista_consulta()
            codigo_consulta = self.__tela_consulta.seleciona_consulta()
            consulta = self.pega_consulta_por_codigo(codigo_consulta)

            if consulta is not None:
                novos_dados_consulta = self.__tela_consulta.pega_dados_consulta()
                consulta.data = novos_dados_consulta["data"]
                consulta.horario = novos_dados_consulta["horario"]
                consulta.descricao = novos_dados_consulta["descricao"]
                consulta.animal = novos_dados_consulta["codigo_animal"]
                consulta.servico = novos_dados_consulta["codigo_servico"]
                self.__consulta_DAO.update(consulta)
                self.lista_consulta()
            else:
                raise ObjetoNaoEncontradoException("Código de Consulta")
            
        except ObjetoNaoEncontradoException as e:
            self.__tela_consulta.mostra_mensagem(e)
        except ListaVaziaException as e: 
            self.__tela_consulta.mostra_mensagem(e)

    def lista_consulta(self):
        dados_consultas = []
        try:   
            if self.__consulta_DAO.get_all() == None:
                raise ListaVaziaException("consultas")
            for consulta in self.__consulta_DAO.get_all():
                dados_consultas.append({"data": consulta.data, "horario": consulta.horario, "descricao": consulta.descricao, "animal": consulta.animal, "servico":consulta.servico, "codigo": consulta.codigo})
            self.__tela_consulta.mostra_consulta(dados_consultas)

        except ListaVaziaException as e:
            self.__tela_consulta.mostra_mensagem(e)

    def excluir_consulta(self):
        try:
            if self.__consulta_DAO.get_all() == None:
                raise ListaVaziaException("consultas")
            self.lista_consulta()
            codigo_consulta = self.__tela_consulta.seleciona_consulta()
            consulta = self.pega_consulta_por_codigo(codigo_consulta)

            if consulta is not None:
                self.__consulta_DAO.remove(consulta.codigo)
                self.lista_consulta()
            else:
                raise ObjetoNaoEncontradoException("Código de Consulta")        
        
        except ObjetoNaoEncontradoException as e:
            self.__tela_consulta.mostra_mensagem(e) 
        except ListaVaziaException as e:
            self.__tela_consulta.mostra_mensagem(e)          
    
    def exibir_detalhes(self):
        try:
            if self.__consulta_DAO.get_all() == None:
                raise ListaVaziaException("consultas")
            self.lista_consulta()
            codigo_consulta = self.__tela_consulta.seleciona_consulta()
            consulta = self.pega_consulta_por_codigo(codigo_consulta)

            if consulta is not None:                
                self.__tela_consulta.mostra_mensagem(f"Consulta em {consulta.data.strftime("%d/%m/%Y")} no horário {consulta.horario} para {consulta.animal.nome_animal}. Descrição: {consulta.descricao}. Serviço: {consulta.servico.nome}.")

            else:
                raise ObjetoNaoEncontradoException("Código de Consulta")
        except ObjetoNaoEncontradoException as e:
            self.__tela_consulta.mostra_mensagem(e)
        except ListaVaziaException as e:
            self.__tela_consulta.mostra_mensagem(e)      
           
    def gerar_relatorio(self):
        locale.setlocale(locale.LC_TIME, "pt_BR.utf8")
        try:
            if self.__consulta_DAO.get_all() == None:
                raise ListaVaziaException("consultas")
            
            data_inicio, data_fim = self.__tela_consulta.solicita_periodo()

            contagem_meses = {}
            contagem_especies = {}
            contagem_racas = {}
            contagem_servicos = {}

            for consulta in self.__consulta_DAO.get_all():                
                if data_inicio <= consulta.data <= data_fim:
                    mes = consulta.data.strftime("%B %Y").lower()
                    especie = consulta.animal.especie.lower()
                    raca = consulta.animal.raca.lower() 
                    servico = consulta.servico.nome.lower()

                    contagem_meses[mes] = contagem_meses.get(mes, 0) + 1
                    contagem_especies[especie] = contagem_especies.get(especie, 0) + 1
                    contagem_racas[raca] = contagem_racas.get(raca, 0) + 1
                    contagem_servicos[servico] = contagem_servicos.get(servico, 0) + 1

            mes_mais_consultas = max(contagem_meses, key=contagem_meses.get, default="sem dados")
            especie_mais_consultada = max(contagem_especies, key=contagem_especies.get, default="sem dados")
            raca_mais_consultada = max(contagem_racas, key=contagem_racas.get, default="sem dados")
            servico_mais_realizado = max(contagem_servicos, key=contagem_servicos.get, default="sem dados")

            def formatar_contagem(nome, contagem):
                return f"{nome} ({contagem} consulta{'s' if contagem != 1 else ''})"

            relatorio_mes = formatar_contagem(mes_mais_consultas, contagem_meses.get(mes_mais_consultas, 0))
            relatorio_especie = formatar_contagem(especie_mais_consultada, contagem_especies.get(especie_mais_consultada, 0))
            relatorio_raca = formatar_contagem(raca_mais_consultada, contagem_racas.get(raca_mais_consultada, 0))
            relatorio_servico = formatar_contagem(servico_mais_realizado, contagem_servicos.get(servico_mais_realizado, 0))

           
            self.__tela_consulta.mostra_relatorio(relatorio_mes, relatorio_especie, relatorio_raca, relatorio_servico)

        except ListaVaziaException as e:
            self.__tela_consulta.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_consulta, 2: self.alterar_consulta, 3: self.lista_consulta, 4: self.excluir_consulta, 5: self.exibir_detalhes, 6: self.gerar_relatorio, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_consulta.tela_opcoes()]()

    