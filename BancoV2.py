class Banco:
    def __init__(self):
        self.saldo = 0
        self.num_saque = 0
        self.extrato = ""

    def deposito(self):
        valor = float(input("Digite o valor que deseja depositar: R$"))
        
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito de R${valor:.2f} \n"
            print(f"\n Depósito de R${valor:.2f} realizado com sucesso.")
        
        else:
            print("Valor de depósito inválido. Por favor, insira um valor positivo.")

    def saque(self):
        if self.num_saque >= 3:
            print("Você ultrapassou o limite de de 3 saques diários.")
            return
        
        valor = float(input("Digite o valor que deseja sacar: R$"))
        if valor < 0:
            print("Valor digitado inválido, digite um número positivo")
        elif valor > 500:
            print("Limite de R$500.00 por saque ultrapassado")
        elif valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            self.num_saque += 1
            self.extrato += f"Saque de R${valor:.2f} \n"
            print(f"\n Saque de R${valor} realizado com sucesso")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo}")
        print("==========================================")

def menu():
        conta = Banco()

        while True:
            MENU = """
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [0] Sair
            --> """
            opcao = input(MENU)

            if opcao == '1':
                conta.deposito()
            elif opcao == '2':
                conta.saque()
            elif opcao == '3':
                conta.exibir_extrato()
            elif opcao == '0':
                break
            else:
                print("Digite uma opção válida")

menu()
