class VendaEmAndamentoException(Exception):
    def __init__(self):
        super().__init__("Já existe uma venda em andamento.")
