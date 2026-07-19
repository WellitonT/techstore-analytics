import json

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def aplicar_desconto(self, percentual):
        if percentual >= 0 and percentual <= 100:
          self.valor = self.valor * (1 - percentual / 100)
        else:
           print("Percentual inválido!")

def salvar_catalogo(produtos: list, caminho:str):
    lista_catalogo = []
    for produto in produtos:
        lista_catalogo.append({"nome": produto.nome, "valor": produto.valor})

    with open(caminho, "w") as f:
        json.dump(lista_catalogo, f, indent=4)

catalogo = [
    Produto("Notebook Acer Nitro", 7500.0),
    Produto("Mouse Havit", 150.0),
    Produto("Monitor AOC", 1200.0),
    Produto("Teclado Redragon", 300.0),
    Produto ("Headset Havit", 200.0),
    Produto("Iphone 17 Pro Max", 12500.0),
    Produto("MacBook Air 15", 21700.0),
    Produto("Processador Ryzen 9", 4900.0)
]

salvar_catalogo(catalogo, "catalogo.json")

def carregar_catalogo(caminho: str) -> list:
    try:
        with open(caminho) as f:
            dados = json.load(f)

        lista_dados = []

        for dado in dados:
            lista_dados.append(Produto(dado["nome"], dado["valor"]))

        return lista_dados
    except FileNotFoundError:
        return []

def criar_produto_seguro(nome, valor):
    try:
        valor_convertido = float(valor)
    except ValueError:
        print("Valor inválido para produto")
        return None

    return Produto(nome, valor_convertido)            

def estatisticas_catalogo(produtos: list) -> dict:
    if len(produtos) == 0:

        return {
        "produto_mais_caro": None,
        "produto_mais_barato": None,
        "valor_total": 0,
        "ticket_medio": 0
    }

    mais_caro = produtos[0]
    mais_barato = produtos[0]

    for produto in produtos:
        if produto.valor > mais_caro.valor:
            mais_caro = produto
        if produto.valor < mais_barato.valor:
            mais_barato = produto

    valor_total = sum(produto.valor for produto in produtos)
    quantidade = len(produtos)

    try:
        ticket_medio = valor_total / quantidade
    except ZeroDivisionError:
        ticket_medio = 0

    return {
        "produto_mais_caro": mais_caro,
        "produto_mais_barato": mais_barato,
        "valor_total": valor_total,
        "ticket_medio": ticket_medio
    }    

def atualizar_catalogo(caminho, nome_produto, novo_valor):

    catalogo = carregar_catalogo(caminho)
    encontrado = False

    for produto in catalogo:
        if produto.nome == nome_produto:
            produto.valor = novo_valor
            encontrado = True

    if not encontrado:
        print("Produto não encontrado no catálogo")

    salvar_catalogo(catalogo, caminho)








