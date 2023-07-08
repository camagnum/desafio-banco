from os import system

saudacao = "=============== Seja Bem Vindo! ================"

menu = '''==== Escolha uma das opções para continuar. ====
[e] - Extrato 
[s] - Saque
[d] - Depósito
[q] - Sair

=> '''

extrato = []
limite_diario = 3
saldo = 500.0

print(saudacao)

while True:
    
    opcao = input(menu)
    
    if opcao == "e":
        for operacao in extrato:
            print(item)

    elif opcao == "s":
        print(f"Seu saldo atual é: R${saldo:.2f}.")
        valor = float(input("Qual o valor que deseja sacar?\n"))
        if valor > 0 and valor <= saldo and limite_diario > 0:
            system('clear')
            saldo -= valor
            print(f"===========================\n"
                  f"\nO saque foi de R${valor:.2f}.\n"
                  f"O novo saldo é R${saldo:.2f}."
                 )
            extrato.append(f"-{valor:.2f}")
            limite_diario -= 1
            print(f"\nSaques que ainda pode realizar hoje: {limite_diario}.\n")
        elif valor < 0 or valor > saldo:
            system("clear")
            print("Insira um valor válido.\n")
        elif limite_diario <= 0:
            system("clear")
            print("Excedeu seu limite de saques diários.\n")
        else:
            print("Insira um valor válido.\n")

    elif opcao == "d":
        print(f"Seu saldo atual é: R${saldo:.2f}.")
        valor = float(input("Qual o valor que deseja depositar?\n"))
        if valor > 0:
            system("clear")
            saldo += valor
            print(f"===========================\n"
                  f"\nO depósito foi de R${valor:.2f}.\n"
                  f"O novo saldo é R${saldo:.2f}."
                 )
            extrato.append(f"{valor:.2f}")
        else:
            print("Insira um valor maior que R$0.00 para depositar.")

    elif opcao == "q":
        print('''=======================
Obrigado. Até a próxima!''')
        break

    else:
        print("Insira uma opção válida.\n")

