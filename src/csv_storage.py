import csv
from src.models import Produto
from src.storage_interface import StorageInterface

class CsvStorage(StorageInterface):
    def salvar(self, produtos: list) -> None:
        with open(self.caminho, "w", newline="") as f:
            escritor = csv.DictWriter(f, fieldnames=["nome", "valor"])
            escritor.writeheader()
            for produto in produtos:
                escritor.writerow({"nome": produto.nome, "valor": produto.valor})

    def carregar(self) -> list:
        try:
            produtos = []
            with open(self.caminho) as f:
                leitor = csv.DictReader(f)
                for linha in leitor:
                    produtos.append(Produto(linha["nome"], float(linha["valor"])))
            return produtos
        except FileNotFoundError:
            return []