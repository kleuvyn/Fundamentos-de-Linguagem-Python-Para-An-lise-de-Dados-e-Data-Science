#Exercício 3 - Crie duas strings e concatene as duas em uma terceira string"
nome = str(input('Digite o seu primeiro nome: \n'))
sobrenome = str(input('Digite o seu sobrenome: \n '))
nome_completo = nome + sobrenome
print('Olá {}'.format(nome_completo))