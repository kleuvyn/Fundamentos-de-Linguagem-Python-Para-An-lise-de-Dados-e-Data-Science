import random
import datetime

class ContaBancaria:

    def __init__(self):
        self.clientes = {}
        self.agencia = "031524"

    def __init__(self, agencia, numero_conta):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = 0
        self.limite = 500
        self.extrato_log = []
        self.numero_do_saque = 0
        self.LIMITE_DO_SAQUE = 3

    def __init__(self, nome_completo, cpf, endereco, email):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.endereco = endereco
        self.email = email
        self.conta = None



    def menu(self):
        return """
[d] = Depositar
[s] = Sacar
[e] = Extrato
[b] = Saldo

[nc] = Nova Conta
[nu] = Novo Usuario
[lc] = Lista Contas
[i] = Sair

=> """

    def criar_conta(self, cpf, email, endereco):
        if cpf not in self.clientes:
            nome = input("Nome Completo: ")
            self.clientes[cpf] = {"nome": nome, "email": email, "endereco": endereco}
            num_conta = str(random.randint(1000, 9999))
            self.clientes[cpf]["conta"] = {"agencia\n": self.agencia, "numero\n": num_conta, "saldo\n": 0, "extrato\n": [], "numero_do_saque\n": 0, "ultimo_saque\n": None}
            print("Usuário e conta criados com sucesso.")
            print(f"Agência: {self.agencia}, Número da Conta: {num_conta}")
        else:
            print("Cliente já existe com esse CPF.")


    def sacar(self, cpf, valor):
        if cpf in self.clientes:
            conta = self.clientes[cpf].get("conta")
            if conta:
                today = datetime.date.today()
                ultimo_saque = conta.get("ultimo_saque")
                if ultimo_saque is None or ultimo_saque != today:
                    if conta["numero_do_saque"] < 3:
                        if 0 < valor <= conta["saldo"]:
                            conta["saldo"] -= valor
                            conta["extrato"].append(f"Saque: R${valor:.2f}")
                            conta["numero_do_saque"] += 1
                            conta["ultimo_saque"] = today
                            print(f"Saque de R${valor:.2f} realizado com sucesso.")
                        else:
                            print("Saldo insuficiente.")
                    else:
                        print("Limite de saques já atingido para hoje.")
                else:
                    print("Limite de saques já atingido para hoje.")
            else:
                print("Cliente não possui conta associada.")
        else:
            print("Cliente não encontrado com esse CPF.")



def main():
    conta = ContaBancaria()

    while True:
        opcao = input(conta.menu())

        if opcao == "d":
            cpf = input("Informe o CPF do titular da conta (somente números): ")
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(cpf, valor)
        elif opcao == "s":
            cpf = input("Informe o CPF do titular da conta (somente números): ")
            valor = float(input("\nInforme o valor do saque: "))
            conta.sacar(cpf, valor)
        elif opcao == "e":
            cpf = input("Informe o CPF do titular da conta (somente números): ")
            conta.extrato(cpf)
        elif opcao == "b":
            cpf = input("Informe o CPF do titular da conta (somente números): ")
            conta.saldo(cpf)
        elif opcao == "nc":
            cpf = input("Informe o CPF do titular da conta (somente números): ")
            email = input("E-mail do titular da conta: ")
            endereco = input("Endereço do titular da conta: ")
            conta.criar_conta(cpf, email, endereco)
        elif opcao == "nu":
            cpf = input("CPF do titular da nova conta (somente números): ")
            if cpf not in conta.clientes:
                nome = input("Nome Completo: ")
                email = input("E-mail: ")
                endereco = input("Endereço: ")
                conta.clientes[cpf] = {"nome": nome, "email": email, "endereco": endereco}
                print("Usuário criado com sucesso.")
                num_conta = str(random.randint(1000, 9999))
                conta.clientes[cpf]["conta\n"] = {"agencia\n": conta.agencia, "numero\n": num_conta, "saldo\n": 0, "extrato\n": [], "numero_do_saque\n": 0, "ultimo_saque\n": None}
                print(f"Agência: {conta.agencia}, Número da Conta: {num_conta}")
            else:
                print("Cliente já existe com esse CPF.")
        elif opcao == "lc":
            conta.lista_contas()
        elif opcao == "i":
            break
        else:
            print("\nOpção inválida.\n")

if __name__ == "__main__":
    main()