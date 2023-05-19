import textwrap
from abc import ABC, abstractclassmethod, abstractproperty


class Cliente():
    """Representa um cliente de banco"""
    def __init__(self, endereco):
        self._endereco = endereco
        self.contas = []
        
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_contas(self,conta):
        self._contas.append(conta)
    

class PessoaFisica(Cliente):
    """Guarda informações sobre dados de pessoa fisica do cliente"""
    def __init__(self, nome, b_day, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self.b_day = b_day
        self.cpf = cpf

class Conta():
    """Representa uma conta básica"""
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._agencia = "0001"
        self._historico = Historico()
    
    @classmethod
    def nova_conta (cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def historico(self):
        return self._historico
    
    
    def sacar (self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Saldo insuficiente")

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado")
            return True
        else:
            print("Operação inválida")

            return False

        

    def depositar (self, valor):
       if valor > 0:
           self._saldo += valor
           print("Depósito realizado") 
       else:
           print("Operação inválida.")
           return False
       
       return True
        

class ContaCorrente(Conta):
    """Representa uma conta corrente herdeira de Conta"""
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"]== Saque.__name__]
        )
        over_limit = valor > self._limite
        over_saques = numero_saques >= self._limite_saques

        if over_limit:
            print("Operação inválida.Valor de saque excede o limite da conta")
        
        elif over_saques:
            print("Limite de saques atingido")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """



class Historico():
    """Represnta um histórico que funciona como um extrato para contas."""
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def realizar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )


class Transacao(ABC):
    """Interface para transações de contas"""
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self,conta):
        pass

class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        succ_transacao = conta.sacar(self.valor)

        if succ_transacao:
            conta.historico.realizar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        succ_transacao = conta.depositar(self.valor)

        if succ_transacao:
            conta.historico.realizar_transacao(self)



def menu():
    menu  = """\n
    ******MENU******
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Cliente
    [5] Nova Conta Corrente
    [0] Sair

    """
    return input(textwrap.dedent(menu))

def f_cliente(cpf,clientes):
    frd_clients = [cliente for cliente in clientes if cliente.cpf==cpf]
    return frd_clients[0] if frd_clients else None


def retrieve_conta(cliente):
    if not cliente.contas:
        print("\nCliente não posssui uma conta")
        return
    
    #FIXME: não permite escolha de conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF(apenas números):")
    cliente = f_cliente(cpf,clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
    
    valor = float(input("Informe o valor de depósito: "))
    if valor<= 0:
        print("Operação inválida.")
        return
    transacao = Deposito(valor)

    conta = retrieve_conta(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)


def sacar(clientes):
    cpf = input("Informe o CPF(apenas números):")
    cliente = f_cliente(cpf,clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return
    
    valor = float(input("Informe o valor de saque: "))
    transacao = Saque(valor)

    conta = retrieve_conta(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF(apenas números):")
    cliente = f_cliente(cpf,clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return
    
    conta = retrieve_conta(cliente)
    if not conta:
        return
    
    print("\n######EXTRATO######")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não há movimentações"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("#############")


def criar_cliente(clientes):
    cpf = input("Informe o CPF(apenas números):")
    cliente = f_cliente(cpf,clientes)

    if cliente:
        print("Já existe um cliente cadastrado com este CPF.")
        return
    
    nome = input("Informe seu nome completo: ")
    b_day = input("Informe sua data de nascimento [dd/mm/aaaa]: ")
    addr_st = input("Informe Endereço- nome da rua: ").title()
    addr_nb = int(input("Informe Endereço- logradouro(número): "))
    addr_cst = input("Informe Endereço- cidade e estado: ").title()
    addr_full = f"{addr_st} {addr_nb} {addr_cst}"
    
    cliente = PessoaFisica(nome=nome, b_day=b_day, cpf=cpf, endereco=addr_full )

    clientes.append(cliente)

    print("\nCliente criado com sucesso.")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF(apenas números):")
    cliente = f_cliente(cpf,clientes)

    if not cliente:
        print("\nCliente não encontrado")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com sucesso.")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():

    clientes = []
    contas = []

    while True:
        opcao = int(menu())

        if opcao == 1:
            depositar(clientes)

        elif opcao == 2:
            sacar(clientes)
        
        elif opcao == 3:
            exibir_extrato(clientes)

        elif opcao == 4:
            criar_cliente(clientes)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        #FIXME
       #elif opcao == 6:
            #listar_contas(contas)

        elif opcao == 0:
            break

        else:
            print("\nOperação inválida.")


main()
