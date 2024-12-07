from abc import ABC, abstractmethod
from datetime import datetime
from exceptions.tamanho_insuficiente_exception import TamanhoInsuficienteException
import PySimpleGUI as sg

class AbstractTela(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    def validar_tamanho(self, valor, campo, min_tamanho=0, max_tamanho=None):
        if len(valor) < min_tamanho:
            raise TamanhoInsuficienteException(campo, min_tamanho)
        if max_tamanho is not None and len(valor) > max_tamanho:
            raise ValueError(f"O campo '{campo}' deve ter no máximo {max_tamanho} caracteres.")

    def validar_apenas_digitos(self, valor, campo):
        if not valor.isdigit():
            raise ValueError(f"O campo '{campo}' deve conter apenas dígitos.")

    def validar_apenas_letras(self, valor, campo):
        if not valor.replace(" ", "").isalpha():
            raise ValueError(f"O campo '{campo}' deve conter apenas letras.")
            
    def le_data(self, valor, campo):
    
        try:
            data_obj = datetime.strptime(valor, "%d/%m/%Y")
            return data_obj
        except ValueError:
            raise ValueError(f"O campo '{campo}' contém uma data inválida! Use o formato DD/MM/AAAA.")
    
    def le_horario(self, valor, campo):     
             try:     
                 horario_obj = datetime.strptime(valor, "%H:%M").time()                           
                 return horario_obj
             except ValueError:
                 raise ValueError(f"O campo '{campo}' contém um horário inválido! Use o formato HH:MM.")