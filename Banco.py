menu = """

[1]Depositar
[2]Sacar
[3]Extrato
[0]Sair

--> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Digite a quantidade que deseja depositar: R$"))
        if valor > 0:
            saldo += valor 
            extrato += f"Deposito: R${valor:.2f}\n"
            print(f"Você depositou {valor} com sucesso")
        else:
            print("Operação Falhou, Tente Novamente!" );

    elif opcao == 2:
        valor = float(input("Digite quanto quer sacar: R$"))

        sem_saldo = valor > saldo

        sem_limite = valor > limite

        sem_saque = numero_saque >= LIMITE_SAQUE

        if sem_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif sem_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif sem_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R${valor:.2f}\n"
            numero_saque -= 1
            print(f"Você sacou {valor} com sucesso")

        else:
            print("Operação falhou! O valor informado é inválido.");

    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================");

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

