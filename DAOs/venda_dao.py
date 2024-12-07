from DAOs.dao import DAO
from entidade.venda import Venda

class VendaDAO(DAO):
    def __init__(self):
        super().__init__('vendas.pkl')

    def add(self, venda: Venda):
        if((venda is not None) and isinstance(venda, Venda) and isinstance(venda.codigo_venda, str)):
            super().add(venda.codigo_venda, venda)   

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    