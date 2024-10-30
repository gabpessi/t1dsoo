class TelaSistema:
     def tela_opcoes(self):
        print("-------- SisSistemas ---------")
        print("Escolha sua opcao")
        print("1 - Serviços")
        print("2 - Produtos")     
        print("3 - Consultas")
        print("4 - Clientes")   
        print("5- Veterinários")
        print("6- Vendas")
        opcao = int(input("Escolha a opcao:"))
        if not isinstance(opcao, int):
            print("Dados incorretos")
            return
        return opcao
