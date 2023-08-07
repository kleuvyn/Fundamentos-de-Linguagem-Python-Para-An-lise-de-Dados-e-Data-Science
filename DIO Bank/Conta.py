class ContaBancaria:

    extrato: str

    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_do_saque = 0
        self.LIMITE_DO_SAQUE = 3

    def menu(self):
        return """
[d] = depositar
[s] = sacar
[e] = extrato
[i] = sair
[b] = saldo
=> """

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R${valor:.2f}\n"
            return True

        else:
            print("Valor inválido para depósito.")
            return False

    def sacar(self, valor):
        if self.numero_do_saque < self.LIMITE_DO_SAQUE:
            if 0 < valor <= self.saldo:
                self.saldo -= valor
                self.extrato += f"Saque: R${valor:.2f}\n"
                self.numero_do_saque += 1
                return True

            else:
                print("Saldo insuficiente.")
                return False

        else:
            print("Limite de saques atingido.")
            return False

    def extrato(self):
        return self.extrato


conta = ContaBancaria()

while True:

    opcao = input(conta.menu())

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        conta.depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        conta.sacar(valor)

    elif opcao == "b":
        print("saldo: \n", conta.saldo)

    elif opcao == "e":
        print("Extrato: \n",conta.extrato)

    elif opcao == "i":
        break

    else:
        print("Opção inválida.")
