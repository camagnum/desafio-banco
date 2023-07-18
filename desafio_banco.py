from os import system
from datetime import date

system("clear")
saudacao = "=============== Seja Bem Vindo! ================"

menu = """\n==== Escolha uma das opções para continuar. ====
[e] - Extrato 
[s] - Saque
[d] - Depósito
[u] - Cadastrar Usuário
[l] - Listar Usuários
[f] - Finalizar

=> """

print(saudacao)

def criar_usuario(usuarios):
    nome = input("Informe o nome completo: ")
    cpf = input("Informe o CPF (apenas os números): ")
    
    cpf_valido = len(cpf) == 11
    
    if cpf_valido:
        usuarios.append({"nome":nome, "cpf": cpf})
        print("=== USUÁRIO CRIADO COM SUCESSO ===")
    else:
        print("=== ERRO ===")
        
def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

def sacar(*, valor, saldo, extrato, data, limite):
    
    valor_numerico = type(valor) != float
    saldo_inferior = valor > saldo
    limite_excedido = valor > 500
    saques_excedidos = limite <= 0
        
    if valor_numerico:
        print("Insira um valor válido.")
    elif valor < 0:
        system("clear")
        print("Insira um valor maior que R$0.00 para depositar.")
    elif saldo_inferior:
        system("clear")
        print(f"Insira um valor inferior a {saldo:.2f}.")
    elif limite_excedido:
        system("clear")
        print("Insira um valor inferior a R$500.00.")
    elif saques_excedidos:
        system("clear")
        print("Excedeu seu limite de saques diários.")
    else:
        system("clear")
        saldo -= valor
        print(
            f"SAQUE REALIZADO COM SUCESSO!\n"
            f"\nO saque foi de R${valor:.2f}.\n"
            f"O novo saldo é R${saldo:.2f}."
        )
        extrato.append(f"{data:%d/%m/%Y}\t\t\t{valor:>10.2f} -")
        limite -= 1
        print(f"\nSaques que ainda pode realizar hoje: {limite}.")
        
    return saldo, extrato, limite

def depositar(valor, saldo, extrato, data, /):
    if valor > 0:
        system("clear")
        saldo += valor
        print(
            f"DEPÓSITO REALIZADO COM SUCESSO!\n"
            f"\nO depósito foi de R${valor:.2f}.\n"
            f"O novo saldo é R${saldo:.2f}."
        )
        extrato.append(f"{data:%d/%m/%Y}\t\t\t{valor:>10.2f} +")
    else:
        system("clear")
        print("Insira um valor maior que R$0.00 para depositar.")
        
    return saldo, extrato
    
def imprime_extrato(saldo, /, *, extrato):
    print("================== EXTRATO ==================")
    print(
        "Não existem movimentações a serem exibidas!"
    ) if not extrato else gerar_extrato(extrato)
    print(f"\nSALDO: R${saldo:.2f}.")
    print("=============================================")
        
def gerar_extrato(extrato):
    for operacao in extrato:
        print(operacao)


def main():
    extrato = []
    saldo = 500.0
    limite_diario = 3
    usuarios = []

    while True:
        d = date.today()
        opcao = input(menu).lower()
        system("clear")

        # EXTRATO
        if opcao == "e":
            imprime_extrato(saldo, extrato=extrato)

        # SAQUE
        elif opcao == "s":
            print(f"Seu saldo atual é: R${saldo:.2f}.")
            valor = float(input("Qual o valor que deseja sacar?\n"))
            saldo, extrato, limite_diario = sacar(valor=valor, saldo=saldo, extrato=extrato, data=d, limite=limite_diario)

        # DEPÓSITO
        elif opcao == "d":
            print(f"Seu saldo atual é: R${saldo:.2f}.")
            valor = float(input("Qual o valor que deseja depositar?\n"))
            saldo, extrato = depositar(valor, saldo, extrato, d)

        # CADASTRAR USUÁRIO
        elif opcao == "u":
            criar_usuario(usuarios)
        
        # LISTAR USUÁRIOS
        elif opcao == "l":
            listar_usuarios(usuarios)
            
        # FINALIZAR
        elif opcao == "f":
            system("clear")
            print("===========================\nObrigado. Até a próxima!\n")
            break

        else:
            print("Insira uma opção válida.")

main()