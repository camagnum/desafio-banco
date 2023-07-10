from os import system
from datetime import date

system("clear")
saudacao = "=============== Seja Bem Vindo! ================"

menu = '''\n==== Escolha uma das opções para continuar. ====
[e] - Extrato 
[s] - Saque
[d] - Depósito
[f] - Finalizar

=> '''

def imprime_extrato(extrato):
    for operacao in extrato:
        print(operacao)

extrato = []
limite_diario = 3
saldo = 500.0

print(saudacao)

while True:
    
    d = date.today()
    opcao = input(menu).lower()
    system("clear")
    
    # EXTRATO
    if opcao == "e":
        print("================== EXTRATO ==================")
        print("Não existem movimentações a serem exibidas!") if not extrato else imprime_extrato(extrato)
        print(f"\nSALDO: R${saldo:.2f}.")
        print("=============================================")

    # SAQUE
    elif opcao == "s":
        print(f"Seu saldo atual é: R${saldo:.2f}.")
        valor = float(input("Qual o valor que deseja sacar?\n"))
        if valor > 0 and valor <= saldo and valor <= 500 and limite_diario > 0:
            system('clear')
            saldo -= valor
            print(f"SAQUE REALIZADO COM SUCESSO!\n"
                  f"\nO saque foi de R${valor:.2f}.\n"
                  f"O novo saldo é R${saldo:.2f}."
                 )
            extrato.append(f"{d:%d/%m/%Y}\t\t\t{valor:>10.2f} -")
            limite_diario -= 1
            print(f"\nSaques que ainda pode realizar hoje: {limite_diario}.")
        elif valor < 0:    
            system("clear")
            print("Insira um valor maior que R$0.00 para depositar.")
        elif valor > saldo:
            system("clear")
            print(f"Insira um valor inferior a {saldo:.2f}.")
        elif valor > 500:
            system("clear")
            print("Insira um valor inferior a R$500.00.")
        elif limite_diario <= 0:
            system("clear")
            print("Excedeu seu limite de saques diários.")
        else:
            print("Insira um valor válido.")
    
    # DEPÓSITO
    elif opcao == "d":
        print(f"Seu saldo atual é: R${saldo:.2f}.")
        valor = float(input("Qual o valor que deseja depositar?\n"))
        if valor > 0:
            system("clear")
            saldo += valor
            print(f"DEPÓSITO REALIZADO COM SUCESSO!\n"
                  f"\nO depósito foi de R${valor:.2f}.\n"
                  f"O novo saldo é R${saldo:.2f}."
                 )
            extrato.append(f"{d:%d/%m/%Y}\t\t\t{valor:>10.2f} +")
        else:
            system("clear")
            print("Insira um valor maior que R$0.00 para depositar.")

    # FINALIZAR
    elif opcao == "f":
        system("clear")
        print('===========================\nObrigado. Até a próxima!\n')
        break

    else:
        print("Insira uma opção válida.")

