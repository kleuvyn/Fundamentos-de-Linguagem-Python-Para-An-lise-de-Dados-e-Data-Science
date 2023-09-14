import random

class ContaBancaria:
    agencia_fixa = "001"  # Agência fixa

    # Dicionário para armazenar CPFs associados às contas
    contas_cpf = {}

    def __init__(self, cpf):
        self.agencia = ContaBancaria.agencia_fixa
        self.numero_conta = self.gerar_numero_conta()
        self.cpf = cpf
        self.saldo = 0
        self.limite = 500
        self.extrato_log = []
        self.numero_do_saque = 0
        self.LIMITE_DO_SAQUE = 3

    def gerar_numero_conta(self):
        # Gera um número de conta aleatório com 6 dígitos
        return str(random.randint(100000, 999999))

    def menu(self):
        return """
        [d] = Depositar
        [s] = Sacar
        [e] = Extrato
        [b] = Saldo
        [i] = Sair
        => """

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato_log.append(f'Depósito: +{valor}')
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor):
        if self.numero_do_saque < self.LIMITE_DO_SAQUE:
            if valor > 0:
                if valor <= self.saldo + self.limite:
                    self.saldo -= valor
                    self.extrato_log.append(f'Saque: -{valor}')
                    self.numero_do_saque += 1
                else:
                    return "Saldo insuficiente!"
            else:
                return "Valor de saque inválido."
        else:
            return "Limite de saques excedido!"

    def extrato(self):
        return "\n".join(self.extrato_log)

    def consultar_saldo(self):
        return f"Saldo atual: {self.saldo}"

    @classmethod
    def criar_conta_com_cpf(cls, cpf):
        # Verifica se o CPF já foi utilizado
        if cpf in cls.contas_cpf:
            return "CPF já está associado a uma conta."
        else:
            nova_conta = cls(cpf)
            cls.contas_cpf[cpf] = nova_conta
            return nova_conta

# Exemplo de uso:
if __name__ == "__main__":
    while True:
        escolha = input("Escolha uma opção:\n[1] - Criar Conta com CPF\n[2] - Acessar Conta Existente\n[3] - Sair\n=> ")

        if escolha == '1':
            cpf = input("Digite o CPF para criar a conta: ")
            resultado = ContaBancaria.criar_conta_com_cpf(cpf)
            if isinstance(resultado, ContaBancaria):
                print(f"Conta criada com sucesso!\nAgência: {resultado.agencia}\nNúmero da Conta: {resultado.numero_conta}\nCPF: {resultado.cpf}")
            else:
                print(resultado)
        elif escolha == '2':
            cpf = input("Digite o CPF para acessar a conta existente: ")
            if cpf in ContaBancaria.contas_cpf:
                conta = ContaBancaria.contas_cpf[cpf]
                print(f"Conta encontrada!\nAgência: {conta.agencia}\nNúmero da Conta: {conta.numero_conta}\nCPF: {conta.cpf}")
                while True:
                    escolha_conta = input(conta.menu())
                    if escolha_conta == 'd':
                        valor = float(input("Digite o valor para depositar: "))
                        resultado = conta.depositar(valor)
                        if resultado:
                            print(resultado)
                    elif escolha_conta == 's':
                        valor = float(input("Digite o valor para sacar: "))
                        resultado = conta.sacar(valor)
                        if resultado:
                            print(resultado)
                    elif escolha_conta == 'e':
                        print(conta.extrato())
                    elif escolha_conta == 'b':
                        print(conta.consultar_saldo())
                    elif escolha_conta == 'i':
                        print("Saindo da conta...")
                        break
                    else:
                        print("Escolha inválida. Tente novamente.")
            else:
                print("CPF não encontrado.")
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")
