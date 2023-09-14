# Entrada de dados
saldo_total = float(input())
valor_saque = float(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
if saldo_total >= valor_saque:
   saldo_disponivel = saldo_total - valor_saque
   print(f"Saque realizado com sucesso! Novo saldo: {saldo_disponivel}")

else:
    print("Saldo insuficiente. Saque não realizado!")
