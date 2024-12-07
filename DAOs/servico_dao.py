from DAOs.dao import DAO
from entidade.servico import Servico

class ServicoDAO(DAO):
    def __init__(self):
        super().__init__('servicos.pkl')

    def add(self, servico: Servico):
        if((servico is not None) and isinstance(servico, Servico) and isinstance(servico.codigo, str)):
            super().add(servico.codigo, servico)

    def update(self, servico: Servico):
        if((servico is not None) and isinstance(servico, Servico) and isinstance(servico.codigo, str)):
            super().update(servico.codigo, servico)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)