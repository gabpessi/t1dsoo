from cliente import Cliente
from produto import Produto
from servico import Servico
from animal import Animal
from veterinario import Veterinario
from consulta import Consulta

class PetShop:
    def __init__(self):
        self.__clientes = []
        self.__servicos = []
        self.__produtos = []
        self.__veterinarios = []
        self.__animais = []

    @property
    def clientes(self):
        return self.__clientes
    
    @clientes.setter
    def clientes(self, clientes: Cliente):
        if not isinstance(clientes, Cliente):
            return
        self.__clientes = clientes

    
    @property
    def servicos(self):
        return self.__servicos
    
    @servicos.setter
    def servicos(self, servicos: Servico):
        if not isinstance(servicos, Servico):
            return
        self.__servicos = servicos
    
    @property
    def produtos(self):
        return self.__produtos
    
    @produtos.setter
    def produtos(self, produtos: Produto):
        if not isinstance(produtos, Produto):
            return
        self.__produtos = produtos

    @property
    def veterinarios(self):
        return self.__veterinarios
    
    @veterinarios.setter
    def veterinarios(self, veterinarios: Veterinario):
        if not isinstance(veterinarios, Veterinario):
            return
        self.__veterinarios = veterinarios

    @property
    def animais(self):
        return self.__animais
    
    @animais.setter
    def animais(self, animais: Cliente):
        if not isinstance(animais, Cliente):
            return
        self.__animais = animais
    

    def cadastrar_cliente(self, nome: str, email: str, telefone: int):
        cliente = Cliente(nome, email, telefone)
        if cliente in self.__clientes:
            return
        self.__clientes.append(cliente)
        return f"Cliente {nome} cadastrado com sucesso!"
    
    def cadastrar_produto(self, nome: str, preco: int, quantidade_estoque: int):
        produto = Produto(nome, preco, quantidade_estoque)
        if produto in self.__produtos:
            return
        self.__produtos.append(produto)

    def listar_produtos(self):
        return [produto.nome for produto in self.__produtos]   
    

    def cadastrar_servico(self, nome: str, preco: int):
        servico = Servico(nome, preco)
        if servico in self.__servicos:
            return
        self.__servicos.append(servico)   

    def listar_servicos(self):
        return[servico.nome for servico in self.__servicos]

    def cadastrar_veterinario(self, nome: str, telefone: int, email: str, especialidade:str):
        veterinario = Veterinario(nome, telefone, email, especialidade)
        if veterinario in self.__veterinarios:
            return
        self.__veterinarios.append(veterinario)

    def cadastrar_animal(self, nome: str, especie: str, raca: str, idade: int):
        animal = Animal(nome, especie, raca, idade)
        if animal in self.__animais:
            return
        self.__animais.append(animal)
    
    
    def cadastrar_consulta(self, data: str, horario: str, descricao: str, servico: Servico, animal: Animal):        
        # Verificar se há veterinários disponíveis
        if not self.__veterinarios:
            return "Nenhum veterinário disponível no momento."
        consulta = Consulta(data, horario, descricao, animal, servico)

        for veterinario in self.__veterinarios:
            if any(c.data == data and c.horario == horario for c in veterinario.consultas):
                return f"Já existe uma consulta agendada para o dia {data} às {horario}."
            
        veterinario_disponivel = self.__veterinarios[0]

        veterinario_disponivel.adicionar_consulta(consulta)

        return consulta
    
    def especie_mais_comum(self):
        if not self.__animais:
            return "Não há animais cadastrados."

        especie_contagem = {}
        for animal in self.__animais:
            if animal.especie in especie_contagem:
                especie_contagem[animal.especie] += 1
            else:
                especie_contagem[animal.especie] = 1

        especie_mais_comum = ''
        maior_contagem = 0

        for especie, contagem in especie_contagem.items():
            if contagem > maior_contagem:
                maior_contagem = contagem
                especie_mais_comum = especie

        return f"A espécie mais comum é '{especie_mais_comum}' com {maior_contagem} animais."    

    def veterinario_com_mais_consultas(self):
        veterinario_mais_consultas = ''
        max_consultas = 0

        # Conta as consultas de cada veterinário
        for veterinario in self.__veterinarios:
            total_consultas = len(veterinario.consultas)
        
            if total_consultas > max_consultas:
                max_consultas = total_consultas
                veterinario_mais_consultas = veterinario

        # Gerar relatório        
        if veterinario_mais_consultas != '':
            return f"{veterinario_mais_consultas}: {max_consultas} consultas"
        else:
            return f"Nenhum veterinário registrou consultas."

    def relatorio_produtos_disponiveis(self):
        if not self.__produtos:
            return "Não há produtos disponíveis."
        
        relatorio = "Produtos disponíveis:\n"
        for produto in self.__produtos:
            relatorio += f"Nome: {produto.nome}, Preço: R${produto.preco:.2f}, Estoque: {produto.quantidade_estoque}\n"
        
        return relatorio