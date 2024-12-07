from DAOs.dao import DAO
from entidade.veterinario import Veterinario

class VeterinarioDAO(DAO):
    def __init__(self):
        super().__init__('veterinarios.pkl')

    def add(self, veterinario: Veterinario):
        if((veterinario is not None) and isinstance(veterinario, Veterinario) and isinstance(veterinario.cpf, str)):
            super().add(veterinario.cpf, veterinario)

    def update(self, veterinario: Veterinario):
        if((veterinario is not None) and isinstance(veterinario, Veterinario) and isinstance(veterinario.cpf, str)):
            super().update(veterinario.cpf, veterinario)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)