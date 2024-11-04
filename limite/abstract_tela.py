from abc import ABC, abstractmethod
from datetime import datetime
from exceptions.tamanho_insuficiente_exception import TamanhoInsuficienteException

class AbstractTela(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    def le_num_inteiro(self, mensagem=" ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:               
                    if isinstance(ints_validos, range):
                        print(f"Valores válidos: {ints_validos.start} a {ints_validos.stop - 1}")
                    else:
                        print(f"Valores válidos: {', '.join(map(str, ints_validos))}")

    def le_string_com_tamanho(self, mensagem=" ", min_tamanho=0, max_tamanho=None, campo="input", somente_digitos=False, somente_letras=False):
        while True:
            valor_lido = input(mensagem)
            try:
                if len(valor_lido) < min_tamanho:
                    raise TamanhoInsuficienteException(campo, min_tamanho)
                if max_tamanho is not None and len(valor_lido) > max_tamanho:
                    raise ValueError(f"O valor para '{campo}' deve ter no máximo {max_tamanho} caracteres.")
                if somente_digitos:
                    self.validar_digitos(valor_lido, campo)
                if somente_letras:
                    self.validar_alpha(valor_lido, campo)
                return valor_lido
            except TamanhoInsuficienteException as e:
                print(e)
            except ValueError as e:
                print(e)

    def validar_email(self, email):
        if len(email) < 5:
            raise TamanhoInsuficienteException("email", 5)
        if "@" not in email or "." not in email:
            raise ValueError("O formato do e-mail é inválido.")

    def le_email(self, mensagem="Email: "):
        while True:
            email = input(mensagem)
            try:
                self.validar_email(email)
                return email
            except TamanhoInsuficienteException as e:
                print(e)
            except ValueError as e:
                print(e)

    def validar_digitos(self, valor, campo):
        if not valor.isdigit():
            raise ValueError(f"O {campo} deve conter apenas dígitos.")

    def validar_alpha(self, valor, campo):
        if not valor.replace(" ", "").isalpha():
            raise ValueError(f"O {campo} deve conter apenas letras.")
        

    def le_data(self, mensagem="Data: "):
        while True:
            data_str = input(mensagem)
            try:                
                data = datetime.strptime(data_str, "%d/%m/%Y")
                return data
            except ValueError:
                print("Data inválida! Use o formato DD/MM/AAAA.")

    def le_horario(self, mensagem="Horário: "):
        while True:
            horario_str = input(mensagem)
            try:                
                horario = datetime.strptime(horario_str, "%H:%M").time()
                return horario
            except ValueError:
                print("Horário inválido! Use o formato HH:MM.")