class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo   # protegido

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
        else:
            print("saldo insuficiente ou valor inválido.")

    def mostrar_saldo(self):
        print(f"saldo de {self.titular}: r$ {self._saldo}")

conta = Conta("bruno", 100)
conta.depositar(50)
conta.sacar(30)
conta.mostrar_saldo()
