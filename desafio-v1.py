menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
n_saques = 0
LIMITE_SAQUES = 3
operacoes = []


def deposito(d, saldo, operacoes):
    if d > 0:
        saldo = saldo + d
        operacoes.append(f"Depósito: R$ +{d:.2f}")
        print("Depósito realizado com sucesso!")
        return saldo
    else:
        print("Depósito inválido!")

def saque(s, n_saques, saldo, operacoes):
    if(n_saques < LIMITE_SAQUES):
        if(s <= 500):
            if(saldo > 0 and s <= saldo):
                saldo -= s
                operacoes.append(f"Saque: R$ -{s:.2f}")
                print("Saque realizado com sucesso!")
                n_saques +=1
                return saldo, n_saques
            else:
                print("Saldo insuficiente!")
        else:
            print("Valor limite de saque excedido!")
    else:
        print("Limite diário de saque excedido! ")
    
def extrato(saldo, operacoes):
    if(len(operacoes) > 0):
        print(*operacoes, sep = "\n")
        print("")
        print(f"Saldo: R$ {saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.")


while True:
    opcao = input(menu)

    if opcao == "d":
        d = int(input())
        saldo = deposito(d, saldo, operacoes)

    elif opcao == "s":
        s = int(input())
        saldo, n_saques = saque(s, n_saques, saldo, operacoes)

    elif opcao == "e":
        extrato(saldo, operacoes)

    elif opcao == "q":
        break
    
    else:
        print("Opção inválida, selecione novamente a operação desejada.")
