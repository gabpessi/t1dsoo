class NenhumaVendaAtivaException(Exception):
    def __init__(self):
        super().__init__("Não há nenhuma venda ativa.")
