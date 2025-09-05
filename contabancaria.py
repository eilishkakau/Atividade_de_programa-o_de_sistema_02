class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para saque.")

    def mostrar_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

conta = ContaBancaria("Maria", 1000)
conta.mostrar_saldo()
conta.depositar(250)
conta.sacar(500)
conta.mostrar_saldo()