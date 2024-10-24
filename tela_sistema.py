class TelaSistema:
     def tela_opcoes(self):
        print("-------- SisSistemas ---------")
        print("Escolha sua opcao")
        print("1 - Serviços")
        print("2 - Produtos")     
        print("3 - Consultas")   
        opcao = int(input("Escolha a opcao:"))
        if not isinstance(opcao, int):
            print("Dados incorretos")
            return
        return opcao
