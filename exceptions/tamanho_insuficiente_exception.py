class TamanhoInsuficienteException(Exception):
    def __init__(self, campo, tamanho_minimo):
        super().__init__(f"O valor para '{campo}' deve ter pelo menos {tamanho_minimo} caracteres.")

