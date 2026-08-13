from dataclasses import dataclass, field
from datetime import date
from uuid import uuid4

# %%
class Produto:
    aliquota = 10    

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    @property
    def valor(self):
        return self._valor  

    @valor.setter
    def valor(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        self._valor = novo_valor      

    # _____APLICAR DESCONTO_____
    def aplicar_desconto(self, percentual):
        if percentual >= 0 and percentual <= 100:
            self.valor = self.valor * (1 - percentual / 100)
        else:
            raise ValueError(f"Percentual inválido: {percentual}. Deve estar entre 0 e 100.")

    # _____CALCULAR IMPOSTO______
    def calcular_imposto(self):
        return self.valor * (self.aliquota / 100)

    def calcular_frete(self):
        return 0.0 # produto sem frete por padrão 

    def calcular_total(self):
        return self.valor + self.calcular_imposto() + self.calcular_frete()       

class ProdutoFisico(Produto):
    aliquota = 15
    frete = 25

    def calcular_frete(self):
        return self.frete

class ProdutoDigital(Produto):
    aliquota = 42

'''fisico = ProdutoFisico(nome="Monitor", valor=750.0)
digital = ProdutoDigital(nome="Ebook", valor=37.0)

print(fisico.calcular_total())
print(digital.calcular_total())'''
p1 = Produto(nome="Mouse", valor=50.0)
print(p1)
print(repr(p1))
print([p1])

try:
    produto_invalido = Produto(nome="Erro", valor=-10)
except ValueError as e:
    print(f"Bloqueado corretamente: {e}")

# @dataclass é um decorador — ele pega essa classe e gera automaticamente
# um monte de código repetitivo que você teria que escrever à mão:
# o __init__, o __repr__ (pra imprimir bonito), entre outros.
# %%
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
