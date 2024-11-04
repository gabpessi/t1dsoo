class ObjetoNaoEncontradoException(Exception):
    def __init__(self, tipo_objeto):
        super().__init__(f"{tipo_objeto} não encontrado.")
