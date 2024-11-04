class ObjetoRepetidoException(Exception):
    def __init__(self, tipo_objeto, identificador):
        super().__init__(f"{tipo_objeto} com identificador '{identificador}' já cadastrado no sistema.")
