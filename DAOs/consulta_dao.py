from DAOs.dao import DAO
from entidade.consulta import Consulta

class ConsultaDAO(DAO):
    def __init__(self):
        super().__init__('consultas.pkl')

    def add(self, consulta: Consulta):
        if((consulta is not None) and isinstance(consulta, Consulta) and isinstance(consulta.codigo, str)):
            super().add(consulta.codigo, consulta)

    def update(self, consulta: Consulta):
        if((consulta is not None) and isinstance(consulta, Consulta) and isinstance(consulta.codigo, str)):
            super().update(consulta.codigo, consulta)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)