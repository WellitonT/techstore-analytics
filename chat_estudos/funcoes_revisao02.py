#Crie uma função maior_valor(produtos: list) -> dict 
#que recebe uma lista de dicionários (mesmo formato de antes: {"Produto": ..., "Valor": ...}) 
# e retorna o dicionário do produto mais caro.

lista_produtos = [
        {"Produto": "Notebook Acer Nitro", "Valor": 10799},
        {"Produto": "Placa de Vídeo RTX 5060 MSI", "Valor": 2599},
        {"Produto": "Monitor AOC", "Valor": 799},
        {"Produto": "Processador Ryzen 7 5700x", "Valor": 1199},
        {"Produto": "Iphone 17 Pro Max", "Valor": 12589}
    ]

def maior_valor(produtos: list) -> dict:
    maior = produtos[0]
    for produto in produtos:
        if produto["Valor"] > maior["Valor"]:
            maior = produto
            
    return maior

print(maior_valor(lista_produtos))
