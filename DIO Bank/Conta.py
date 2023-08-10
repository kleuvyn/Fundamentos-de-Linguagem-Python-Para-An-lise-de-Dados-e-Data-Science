class ContaBancaria:

    def __init__(self):
        self.contas = {}

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

    def criar_cliente(self):
        cpf = input("CPF do titular da nova conta (somente números): ")
        if cpf in self.contas:
            print("Cliente já existe com esse CPF.")
        else:
            self.contas[cpf] = {"saldo": 0, "extrato": [], "numero_do_saque": 0}
            print("Cliente criado com sucesso.")

    def novo_usuario(self):
        cpf = input("CPF do titular da conta (somente números): ")
        if cpf in self.contas:
            nome = input("Nome Completo: ")
            self.contas[cpf]["nome"] = nome
            print("Usuário criado com sucesso.")
        else:
            print("Cliente não encontrado com esse CPF.")

    def lista_contas(self):
        print("Lista de Contas:")
        for cpf, dados in self.contas.items():
            print(f"CPF: {cpf}, Nome: {dados.get('nome', 'Não informado')}")


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