class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def aplicar_desconto(self, percentual):
        self.valor = self.valor * (1 - percentual / 100)

    def resumo(self):
        return f"{self.nome} custa R${self.valor}"

notebook = Produto("Notebook Dell", 3000)
notebook.aplicar_desconto(10)
print(f"Valor com o desconto de 10% = R${notebook.valor}")
print(notebook.resumo())