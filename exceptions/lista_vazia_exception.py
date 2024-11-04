class ListaVaziaException(Exception):
    def __init__(self, tipo_lista, mensagem=None):
        if mensagem is None:
            mensagem = f"A lista de {tipo_lista} está vazia."
        self.mensagem = mensagem
        super().__init__(self.mensagem)