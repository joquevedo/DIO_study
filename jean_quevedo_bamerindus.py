menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 1500
LIMITE_SAQUES = 3
total_saques = 0
extrato =""

while True:
    
    option = int(input(menu))
    
    if option == 1:
        print("Depósito")
        dpt = float(input("Digite o valor para depósito (apenas números): "))
        if dpt > 0:
            saldo += dpt
            extrato+= f"Depósito realizado: R${dpt:.2f}\n"   
        
    elif option == 2:
        if saldo<= 0:
            print("Saldo insuficiente")
        elif LIMITE_SAQUES <= 0:
            print("Você atingiu o seu limites de saques diários.\n Escolha outra opção")
        else:
            print("Sacar")
            saque = float(input("Digite o valor para depósito (apenas números): "))
            if saque > saldo:
                print("Saldo insuficiente")
            elif saque< 0:
                print("Operação inválida")
            else:
                saldo = saldo - saque
                extrato+= f"Saque realizado: R${saque:.2f}\n"
                total_saques +=1
                LIMITE_SAQUES -= 1
        
    elif option== 3:
            print("Extrato")
            extrato += f"Saldo atual: R${saldo:.2f}\n"
            extrato += f"Total de saques no dia: {total_saques}. Limite diário: 3\n"
            print(extrato)
        
    elif option== 0:
        break
    
    else:
        print("Operação ínvalida, selecione novamente a opção desejada")
        
