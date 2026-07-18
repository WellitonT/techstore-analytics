class ContaBancaria:
    def __init__(self, titular:str, saldo:float=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
        else:
            print("Saldo insuficiente")    
        return self.saldo

    def extrato(self):
        return f"{self.titular} tem R${self.saldo}"

conta01 = ContaBancaria("Welliton", 46000)
print(conta01.sacar(5000))
print(conta01.depositar(1200))
print(conta01.extrato())