lista_produtos = [
    {"Produto": "Notebook", "Valor": 3500.0},
    {"Produto": "Mouse", "Valor": 50.0},
    {"Produto": "Monitor", "Valor": 800.0},
]

def buscar_produto(produtos, nome) -> list:
    lista = []
    for produto in produtos:
        if produto["Produto"] == nome:
            return produto["Valor"]

    return "Produto não encontrado"

print(buscar_produto(lista_produtos, "Mouse"))

