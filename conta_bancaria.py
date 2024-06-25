class ContaBancaria:
    def __init__(self, saldo_inicial = 0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo+=valor

    def sacar(self, valor):
        if valor<=self.saldo:
            self.saldo-=valor
            return valor
        else:
            print("Saldo insuficiente")
            return 0

    def printar_saldo(self):
        print(f"Saldo: {self.saldo}")

conta = ContaBancaria(100)
conta.printar_saldo()  # Saldo: 100
conta.depositar(50)
conta.printar_saldo()  # Saldo: 150
conta.sacar(70)
conta.printar_saldo()  # Saldo: 80