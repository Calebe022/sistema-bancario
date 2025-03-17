menu = """  
[a] Depositar  
[b] Sacar  
[c] Extrato  
[d] Sair  

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "a":
        valor = float(input("Por favor, informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Erro: O valor informado é inválido. Operação não concluída!")

    elif opcao == "b":
        valor = float(input("Por favor, informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Erro: Saldo insuficiente. Operação não concluída!")

        elif excedeu_limite:
            print("Erro: O valor do saque excede o limite. Operação não concluída!")

        elif excedeu_saques:
            print("Erro: Número máximo de saques excedido. Operação não concluída!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Erro: O valor informado é inválido. Tente novamente!")

    elif opcao == "c":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "d":
        print("Agradecemos por utilizar nosso sistema bancário. Até breve!")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a opção desejada.")