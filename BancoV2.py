def menu():
    MENU = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
--> """
    return input(MENU)

def deposito(valor, saldo, extrato):
    saldo += valor 
    extrato += f"Depósito de R${valor}\n"
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saque):
    sem_saldo = valor > saldo
    sem_limite = valor > limite
    sem_saque = numero_saque >= 3

    if sem_saldo:
        print(f"Você não tem saldo suficiente");

    elif sem_limite:
        print(f"Você ultrapassou o limite máximo de R$500.00");

    elif sem_saque:
        print("Você ultrapassou o limite de saques");

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque R${valor:.2f} realizado \n"
        numero_saque += 1

    else:
        print("Operação falhou, o valor digitado é inválido")

    return saldo, extrato

def exibir_extrato(saldo, extrato,):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato.strip())
    print(f"\nSaldo: R$ {saldo}")
    print("==========================================")

def control():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    limite_saque = 3

    while True:
        try:
            opcao = int(menu())
        except ValueError:
            print("Digite um número válido")
            continue

        if opcao == 1:
            try:
                valor = float(input("Digite a quantidade para depositar: "))
            except ValueError:
                print("Por favor, insira um valor numérico.")
                continue
            saldo, extrato = deposito(valor, saldo, extrato)

        elif opcao == 2:
            try:
                valor = float(input("Digite a quantidade para sacar: "))
            except ValueError:
                print("Por favor, insira um valor numérico.")
                continue
            if valor > 0:
                saldo, extrato = saque(
                    valor = valor, 
                    saldo = saldo, 
                    limite = limite, 
                    extrato = extrato, 
                    numero_saque = numero_saque)
            else:
                print("Por favor, insira um valor maior que zero para o saque.")

        elif opcao == 3:
            exibir_extrato(saldo, extrato,)

        elif opcao == 0:
            break

        else:
            print("Opção Inválida, tente novamente")

control()
