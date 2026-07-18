lista_produtos = [
    {"Produto": "Iphone 17", "Valor": 9350.0},
    {"Produto": "Samsung Galaxy S30", "Valor": 8500.0},
    {"Produto": "Xiaomi Mi 13", "Valor": 6500.0},
    {"Produto": "Motorola Edge 40", "Valor": 4500.0},
    {"Produto": "Tinta Preta à base d'água", "Valor": -150.0},
    {"Produto": "Monitor LG 27", "Valor": 1200.0},
    {"Produto": "Teclado Mecânico Razer", "Valor": 800.0},
    {"Produto": "Mouse Logitech G Pro", "Valor": 600.0},
    {"Produto": "Fone de Ouvido Sony WH-1000XM4", "Valor": 1500.0},
    {"Produto": "Cadeira Gamer DXRacer", "Valor": 2000.0},
    {"Produto": "Mesa Gamer Pichau", "Valor": 1000.0}
]

def analisar_vendas(lista_produtos: list, minimo: float = 0):
    vendas_filtradas = []
    for produto in lista_produtos:
        if produto["Valor"] > minimo:
            vendas_filtradas.append(produto)
        # ↑ o for termina aqui (note a indentação voltando)

    quantidade = len(vendas_filtradas)
    total_vendas = sum(produto["Valor"] for produto in vendas_filtradas)

    if quantidade > 0:
        media_vendas = total_vendas / quantidade
    else:
        media_vendas = 0

    return {"Total": total_vendas, "Média": media_vendas, "Quantidade": quantidade}

print(analisar_vendas(lista_produtos, minimo=0))  
    