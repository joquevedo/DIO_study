#"""Functions"""
def menu():
    #Menu option
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova Conta Corrente
    [6] Listar usuários
    [7] Listar contas
    [0] Sair

    """
    return input(menu)
#Depósito
"""Deposita valores na conta"""

def deposit_(valor, saldo, extrato, /):
    print(f"Saldo atual: {saldo}\n")
    print(f"###EXTRATO###\n{extrato}\n")

#Saque
"""Saca valores da conta"""

def saq_(*, valor, saldo, extrato):
    print(f"Saldo atual: {saldo}\n")
    print(f"###EXTRATO###\n{extrato}\n")

#Extrato
"""Exibe movimentações na conta"""

def ext_(saldo, /, extrato):
    print(f"Saldo atual: {saldo}\n")
    print(f"###EXTRATO###\n{extrato}\n")
    
#Novo usuário
"""Cria um novo usuário por CPF"""

def new_user(users):
    usr_cpf = input("Digite seu CPF (apenas números): ")
    usr = user_fltr(usr_cpf, users)
    
    if usr:
        print("Usuário já existente. Apenas um CPF por usuário")
        return
        
    usr_name = input("Digite seu nome completo: ").title()
    usr_bday = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    usr_addr_st = input("Endereço- nome da rua: ").title()
    usr_addr_nb = int(input("Endereço- logradouro(número): "))
    usr_addr_cst = input("Endereço- cidade e estado: ").title()
    usr_addr_full = f"{usr_addr_st} {usr_addr_nb} {usr_addr_cst}"
    users.append({"nome":usr_name, "data de nascimento": usr_bday, "cpf": usr_cpf, "endereço": usr_addr_full})
    print("Usuário criado com sucesso!")

#Filtro de usuários
"""Verifica usuários existentes"""

def user_fltr (usr_cpf, users):
    filtered_usr= [usr for usr in users if usr["cpf"] == usr_cpf]
    return filtered_usr[0] if filtered_usr else None
    
#Nova conta
"""Cria nova conta corrente para usuários"""
def new_chk_account(agn,acc_nbr, users):
    usr_cpf = input("Informe o CPF: ")
    usr = user_fltr(usr_cpf, users)
    
    if usr:
        print("Conta-corrente criada com sucesso.")
        return{"agencia": agn, "número da conta": acc_nbr, "usuário": usr}
    
    print("Usuário não encontrado")

#Usuários
"""Exibe lista de usuários"""
def show_users(users):
    print(users)

#Contas
"""Exibe lista de contas-corrente"""
def list_accounts(accounts):
    for acc in accounts:
        print(accounts)

#Programa Principal
"""Executa todas as funções"""

def main():
    #"""Variables"""
    v_saldo = 0
    v_limite = 1500
    v_LIMITE_SAQUES = 3
    v_total_saques = 0
    v_extrato =""
    AGENCIA = "0001"
    users= []
    accounts = []
    
    while True:
        option = int(menu())

        if option == 1:
            v_dpt = float(input("Digite o valor para depósito: "))
            if v_dpt >0: 
                valor = v_dpt
                v_saldo += v_dpt
                v_extrato += f"Saldo atual: R${v_saldo:.2f}\n"
                v_extrato += f"Total de saques no dia: {v_total_saques}. Limite diário: 3\n"
                saldo = v_saldo
                extrato = v_extrato
                deposit_(valor, saldo, extrato)
            elif v_dpt<=0:
                print("Operação inválida.")
            else:
                print("Operação inválida.")
                
        elif option == 2:
            if v_saldo <=0:
                print("Saldo insuficiente.")
            
            elif v_LIMITE_SAQUES == 0:
                print("Você atingiu o limite diário de saques. \n")
                print(f"###EXTRATO###\n{v_extrato}")
            else:
                v_sq = float(input("Digite o valor para saque: "))
                if v_sq <=0:
                    print("Operação inválida")
                elif v_sq > v_saldo:
                    print("Saldo insuficiente")
                else:
                    v_saldo -= v_sq
                    v_LIMITE_SAQUES -= 1
                    v_total_saques += 1
                    v_extrato += f"Saldo atual: R${v_saldo:.2f}\n"
                    v_extrato += f"Total de saques no dia: {v_total_saques}. Limite diário: 3\n"
                    saq_(valor=v_sq, extrato=v_extrato, saldo=v_saldo)
                    
        elif option == 3:
            if not v_extrato:
                print("Não foram realizadas movimentações.")
            else:
                print("###EXTRATO###\n")
                saldo = v_saldo
                ext_(saldo, extrato=v_extrato)
                
        elif option == 4:
            new_user(users)
            
        elif option == 5:
            acc_nbr = len(accounts) + 1
            account = new_chk_account(AGENCIA, acc_nbr, users)
            
            if account:
                accounts.append(account)
    
        elif option == 6:
            show_users(users)
            
        elif option == 7:
            list_accounts(accounts)
            
        elif option == 0:
            break
        
        else:
            print("Operação inválida")
    

main()
