class ContaBancaria:
    def __init__(self, saldo_inicial = 0):
        self.saldo = saldo_inicial
    
    def depositar(self, valor): # Função para depositar dinheiro
        if valor>0: # Verifica se o valor é vakido
            self.saldo+=valor   # Adiciona o valor na conta
            print(f"Deposito de R${valor} realizado com sucesso")
        else:
            print("Valor de depósito inválido")
    
    def sacar(self, valor): # Função para retirar dinheiro da conta
        if valor>0:     
            if valor<=self.saldo: # Verifica se tem dinheiro suficiente na conta para retirar o valor desejado 
                self.saldo-=valor # Saca o valor desejado 
                print(f"Saque de R${valor} realizado com sucesso")
            else:
                print("Saldo insuficiente")
                return 0
        else:
            print("Valor de saque inválido")
    
    def printar_saldo(self): # Função para mostrar o saldo na conta 
        print(f"Saldo: {self.saldo}")

class Banco:    
    def __init__(self):
        self.contas = [] # A instância de Banco é inicializada abrindo uma lista de contas bancárias
        

    def abrir_conta(self, titular, codigo, saldo_inicial = 0):  # Abre uma nova conta bancária
        nova_conta = ContaBancaria(titular, codigo, saldo_inicial)  # Cria uma instancia de conta bancaria 
        self.conta.append(nova_conta)   # Adiciona a nova conta na lista de contas bancarias do Banco
        print(f"Conta de {self.titular} aberta com sucesso")
        print("Saldo inicial:", saldo_inicial)

    def encontrar_conta(self, titular): # Procura uma conta pelo nome do titular
        for conta in self.contas:   # Percorre a lista de contas bancarias do Banco
            if conta.titular == titular: # Verifica se o nome do titular da conta atual é igual ao nome do titular desejado
                return conta
        return None # Se o nome do titular nao for encontrado na lista

    def fechar_conta(self, titular):    # Encerra uma conta bancaria 
        conta = self.encontrar_conta(titular)   # Encontra a conta desejada
        if conta:   # Se a conta existir esse escopo é executado
            self.contas.remove(conta)   # Remove a conta da lista de contas bancarias do banco
            print(f"Conta de {titular} fechada com sucesso")
        else:
            print("Conta não encontrada")


conta = ContaBancaria(100)
conta.printar_saldo()  # Saldo: 100
conta.depositar(50)
conta.printar_saldo()  # Saldo: 150
conta.sacar(70)
conta.printar_saldo()  # Saldo: 80
conta.depositar(125)