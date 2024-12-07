from DAOs.dao import DAO
from entidade.produto import Produto

class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__('produtos.pkl')

    def add(self, produto: Produto):
        if((produto is not None) and isinstance(produto, Produto) and isinstance(produto.codigo, str)):
            super().add(produto.codigo, produto)

    def update(self, produto: Produto):
        if((produto is not None) and isinstance(produto, Produto) and isinstance(produto.codigo, str)):
            super().update(produto.codigo, produto)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)