class QuantidadeInsuficienteException(Exception):
    def __init__(self):
        super().__init__("A quantidade do produto é insuficiente.")