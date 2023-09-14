valor = float(input())

if valor > 0:
    saldo = valor
    print("Depósito realizado com sucesso!")
    print(f"Saldo atual: R$ {saldo:.2f}")
elif valor == 0:
    print("Valor inválido! Digite um valor maior que zero.")
else:
    print("Encerrando o programa...")
