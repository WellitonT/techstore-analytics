from dataclasses import dataclass, field
from datetime import date
from uuid import uuid4
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def aplicar_desconto(self, percentual):
        if percentual >= 0 and percentual <= 100:
            self.valor = self.valor * (1 - percentual / 100)
        else:
            print("Percentual inválido!")

# @dataclass é um decorador — ele pega essa classe e gera automaticamente
# um monte de código repetitivo que você teria que escrever à mão:
# o __init__, o __repr__ (pra imprimir bonito), entre outros.
@dataclass
class Pedido:
    cliente: str
    valor: float 
    status: str = "Pendente"

    # por que date.today() com parênteses trava o valor
    data_pedido: date = field(default_factory=date.today) # <- repare aqui

    # por que field(default_factory=...) resolve isso, chamando a função a cada instância
    # por que default_factory precisa de uma referência a função, não um valor já calculado
    # e agora, o que quebra quando você confunde os dois, e por quê
    id_pedido: str = field(default_factory=lambda: str(uuid4()))


p1 = Pedido(cliente="Ana", valor=100.0)
p2 = Pedido(cliente="Bruno", valor=50.0)