import random

class ContaBancaria:

    def __init__(self):
        self.contas = {}
        self.agencia = "326644"

    def menu(self):
        return """
[d] = Depositar
[s] = Sacar
[e] = Extrato
[b] = Saldo+

[nc] = Nova Conta
[nu] = Novo Usuario
[lc] = Lista Contas
[i] = Sair

=> """

    def novo_usuario(self):
        cpf = input("CPF do titular da nova conta (somente números): ")
        if cpf in self.contas:
            print("Cliente já existe com esse CPF.")
        else:
            nome = input("Nome Completo: ")
            endereco = input("Endereço: ")
            email = input("E-mail: ")
            numero_conta = self.gerar_numero_conta()
            self.contas[cpf] = {"nome": nome, "saldo": 0, "extrato": [], "numero_conta": numero_conta, "endereco": endereco, "email": email}
            print("Cliente criado com sucesso.")

    def gerar_numero_conta(self):
        return str(random.randint(10000, 99999))


    def lista_contas(self):
        print("Lista de Contas:")
        for cpf, dados in self.contas.items():
            print(f"CPF: {cpf}, Nome: {dados.get('nome', 'Não informado')}, Número da Conta: {dados.get('numero_conta', 'Não informado')}, Endereço: {dados.get('endereco', 'Não informado')}, E-mail: {dados.get('email', 'Não informado')}")


def main():
    conta = ContaBancaria()

    while True:
        opcao = input(conta.menu())

        if opcao == "d":
            valor = float(input("\nInforme o valor do depósito: "))
            conta.depositar(valor)
        elif opcao == "s":
            valor = float(input("\nInforme o valor do saque: "))
            conta.sacar(valor)
        elif opcao == "b":
            print("\nSaldo: R$", conta.saldo)
        elif opcao == "e":
            print("\nExtrato:\n", conta.extrato())
        elif opcao == "nc":
            conta.criar_cliente()
        elif opcao == "nu":
            conta.novo_usuario()
        elif opcao == "lc":
            conta.lista_contas()
        elif opcao == "i":
            break
        else:
            print("\nOpção inválida.\n")

if __name__ == "__main__":
    main()

