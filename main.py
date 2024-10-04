opcao = 0
valor_total_saques = float(0)
valor_total_depositos = float(0)
LIMITE_DIARIO_SAQUE = float(500)
max_saque = int(0)
saldo = float(0)
qtd_deposito = int(0)
qtd_saque = int(0)
while True:

    opcao = int(input("""Menu
    [1] Saque
    [2] Deposito
    [3] Saldo
    [4] Sair
    Digite a opção desejada: """))
    if opcao == 4:
        print("-----Extrato-----")
        print("""
        Saldo: R$ {:.2f}
        Quantidade de saques: {:d}
        Quantidade de depositos: {:d}
        Total de saques: R$ {:.2f}
        Total de Depositos: R$ {:.2f}
        """.format(saldo, qtd_saque, qtd_deposito, valor_total_saques, valor_total_depositos))
        print("-----Saindo-----")
        break
    elif opcao == 1:
        print("-----Realizar saque-----")
        print("Saldo: R$", saldo)
        if saldo <= 0:
            print("Sem saldo para saque. Realize um deposito")
        else:
            valor = float(input("Quanto quer sacar? "))
            if valor > LIMITE_DIARIO_SAQUE or valor_total_saques == LIMITE_DIARIO_SAQUE:
                print("Impossivel realizar ação. Limite diario de saque atingido")
                print("Limite de saque: ", LIMITE_DIARIO_SAQUE)
                print("valor ja sacado: ", valor_total_saques)
            elif valor >= saldo:
                print("Saldo insuficiente")
            elif max_saque >= 3:
                print("Atingiu a quantidade de saques: ", max_saque)
            else:
                qtd_saque += 1
                max_saque += 1
                valor_total_saques += valor
                saldo -= valor
                print("Saque realizado com sucesso!")
                print("Novo saldo: R$", saldo)
    elif opcao == 2:
        print("-----Realizar deposito-----")
        valor = float(input("Quanto quer depositar? "))
        if valor <= 0:
            print("Digite um valor de deposito valido")
        else:
            qtd_deposito += 1
            saldo += valor
            valor_total_depositos += valor
            print("Deposito realizado com sucesso!")
            print("Novo saldo: R$", saldo)
    elif opcao == 3:
        print("-----Consulta de saldo-----")
        print("Saldo: R$", saldo)
    else:
        print("opcao invalida, tente novamente")
