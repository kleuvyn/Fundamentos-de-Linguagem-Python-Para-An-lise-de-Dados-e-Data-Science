def informar_tempo_estimado_entrega(nome_restaurante, tempo_estimado_entrega):
    mensagem = f'O restaurante {nome_restaurante} entrega em {tempo_estimado_entrega} minutos.'
    return mensagem


nome_restaurante = input("Digite o nome do restaurante desejado: ")
tempo_estimado_entrega = float(input("Digite o tempo estimado de entrega em minutos: "))

mensagem_entrega = informar_tempo_estimado_entrega(nome_restaurante, tempo_estimado_entrega)
print(mensagem_entrega)