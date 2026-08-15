from abc import ABC, abstractmethod
from src.models import Produto
import json

class StorageInterface(ABC):
    def __init__(self, caminho: str):
        self.caminho = caminho

    @abstractmethod
    def salvar(self, produtos: list) -> None:
        ...

    def carregar(self) -> list:
        ...

class JsonStorage(StorageInterface):
    def salvar(self, produtos: list) -> None:
        lista_catalogo = []
        for produto in produtos:
            lista_catalogo.append({"nome": produto.nome, "valor": produto.valor})
        with open(self.caminho, "w") as f:
            json.dump(lista_catalogo, f, indent=4)

    def carregar(self) -> list:
        try:
            with open(self.caminho) as f:
                dados = json.load(f)
            lista_dados = []
            for dado in dados:
                lista_dados.append(Produto(dado["nome"], dado["valor"]))
            return lista_dados
        except FileNotFoundError:
            return []                     