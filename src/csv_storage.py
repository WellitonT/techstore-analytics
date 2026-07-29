import csv
from src.models import Produto

def salvar_catalogo_csv(produtos: list, caminho: str):
    with open(caminho, "w", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=["nome", "valor"])
        escritor.writeheader()
        for produto in produtos:
            escritor.writerow({"nome": produto.nome, "valor": produto.valor})

def carregar_catalogo_csv(caminho: str) -> list:
    try:
        produtos = []
        with open(caminho) as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                produtos.append(Produto(linha["nome"], float(linha["valor"])))
        return produtos
    except FileNotFoundError:
        return []