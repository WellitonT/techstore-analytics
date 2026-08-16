from abc import ABC, abstractmethod
from src.models import Produto
from pathlib import Path
import json

class StorageInterface(ABC):
    def __init__(self, caminho: str):
        self.caminho = Path(caminho)

    @abstractmethod
    def salvar(self, produtos: list) -> None:
        ...

    @abstractmethod
    def carregar(self) -> list:
        ...                   