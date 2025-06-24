#------------------------ Desafio: Sistema Bancário V1 -----------------
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    # opcao = opcao.lower()       # garantir a operação mesmo se o Capslock estiver acionado

    if opcao == "d":        #*************************** DEPOSITAR ******************
        valor = float(input("Informe o valor do depósito: "))

        # valor = input("Informe o valor do depósito: ")
        # #--------------------  Validação da Entrada (sem uso de função) ---------
        #
        # valor = valor.replace(',', '.')     # troca , por . caso digitem errado
        #
        # if valor.isalpha():    # bloquear digitação de texto
        #     print('Digite apenas números')
        #     valor = 0
        #
        # valor = float(valor)
        # if valor != round(valor, 2):        # bloquear digitação de números a mais
        #     print('Os centavos não foram digitados corretamente')
        #     valor = 0

        #-------------------------------------------------------------------------

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":          #*************************** SACAR ********************
        valor = float(input("Informe o valor do saque: "))

        # valor = input("Informe o valor do saque: ")
        # #--------------------  Validação da Entrada (sem uso de função) ---------
        #
        # valor = valor.replace(',', '.')     # troca , por . caso digitem errado
        #
        # if valor.isalpha():    # bloquear digitação de texto
        #     print('Digite apenas números')
        #     valor = 0
        #
        # valor = float(valor)
        # if valor != round(valor, 2):        # bloquear digitação de números a mais
        #     print('Os centavos não foram digitados corretamente')
        #     valor = 0
        #-------------------------------------------------------------------------

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"   # frase para impressão
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":          #*************************** EXTRATO ********************
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)  # imprime frase linha 80
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":          #*************************** SAIR ************************
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")