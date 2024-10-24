from cliente import Cliente
from produto import Produto
from servico import Servico
from animal import Animal
from veterinario import Veterinario
from consulta import Consulta
from petshop import PetShop
from pessoa import Pessoa
from controlador_sistema import ControladorSistema

# Exemplo de uso e testes
if __name__ == "__main__":
    # Criando um PetShop
    petshop = PetShop()

    # Testando o cadastro de clientes
    print(petshop.cadastrar_cliente("João", "joao@email.com", 123456789))
    print(petshop.cadastrar_cliente("Maria", "maria@email.com", 987654321))

    # Testando o cadastro de veterinários
    vet1 = Veterinario("Dra. Maria", 88888888, "maria@email.com", "Dermatologia")
    petshop.cadastrar_veterinario(vet1.nome, vet1.telefone, vet1.email, vet1.especialidade)

    # Testando o cadastro de animais
    animal1 = Animal("Rex", "Cão", "Labrador", 3)
    petshop.cadastrar_animal(animal1.nome, animal1.especie, animal1.raca, animal1.idade)

    # Testando o cadastro de serviços
    servico1 = Servico("Vacinação", 150, 10)
    petshop.cadastrar_servico(servico1.nome, servico1.preco, servico1.codigo)

    # Listar serviços cadastrados
    print("Serviços disponíveis:", petshop.listar_servicos())

   # Testando o cadastro de consultas
    #consulta1 = petshop.cadastrar_consulta("05/10/2024", "14:00", "Consulta de rotina", servico1, animal1, 2233)
    #if consulta1:  # Verificar se consulta1 não é None
    #    print("Consulta cadastrada:", consulta1.exibir_detalhes())
    #else:
     #   print("Erro ao cadastrar consulta.")
    # Listar animais do cliente
    cliente1 = petshop.clientes[0]  # Pegando o primeiro cliente
    cliente1.adicionar_animal(animal1)
    print("Animais do cliente:", cliente1.listar_animais())

    # Verificar se o veterinário tem consultas
    print("Consultas do veterinário:", [c.exibir_detalhes() for c in vet1.consultas])




    ControladorSistema().inicializa_sistema()
