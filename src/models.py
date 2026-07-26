class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def aplicar_desconto(self, percentual):
        if percentual >= 0 and percentual <= 100:
            self.valor = self.valor * (1 - percentual / 100)
        else:
            print("Percentual inválido!")