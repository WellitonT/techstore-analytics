class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)

    def total(self):
        soma = 0

        for item in self.itens:
            soma += item.valor

        return soma

    def listar(self):
        for item in self.itens:
            print(f"{item.nome} - R$ {item.valor}")      

notebook = Produto("Notebook Acer Nitro", 10799)
iphone = Produto("Iphone 17 Pro Max", 12899)
mouse = Produto("Mouse Havit", 79)
compra01 = CarrinhoDeCompras()
compra01.adicionar(iphone)
compra01.adicionar(notebook)
compra01.adicionar(mouse)
print(compra01.total())
compra01.listar()
