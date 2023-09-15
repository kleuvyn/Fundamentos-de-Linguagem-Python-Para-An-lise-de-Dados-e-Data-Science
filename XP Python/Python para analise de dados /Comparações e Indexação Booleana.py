import numpy as np

print("Comparação Booleanas")
a = np.array([[1, 2], [3, 4]])
b = np.array([1.5, 3.5])
s = 3
print(a > a)
print('\n',a > b)

print('Comparação menor:')
print('\n', a < b)
print('\n', a < s)


print('\nComparação menor ou gual:')
print(a <= b)
print('\n', a <= s)

print('\nComparação maior:')
print(a > b)
print('\n', a > s)

print('\nComparação maior ou gual:')
print(a >= b)
print('\n', a >= s)

print('\nComparação de igualdade:')
print(a == b)
print('\n', a == s)

print('\nIndexação Booleana> um novo subarraycontendo uma '
      'copia dos elementos em que a condição de verificar se aplica')
cond = a <= 2
d = a[cond]
print("a:", a)
print('Condição:', cond)
print('d', d)

x = np.array([[1, 2, 3],
            [4, 11,21],
            [42, 8, 9]])
k = 10

condicao = x > k
print('\nx:', x)
print('\nCondição:\n', condicao)
print('\nNúmeros pares\n')

condicao = x % 2 == 0
print('\nCondiçã', condicao)
print('\nNúmeros pares', x[condicao])
print(f'elementos maiores que {k}:', x[condicao])
print(f'numeros de elementos maiores que {k}:', len(x[condicao]))

condicao = x % 2 == 1
print('\nCondiçã', condicao)
print('\nNúmeros impares', x[condicao])
print(f'elementos maiores que {k}:', x[condicao])
print(f'numeros de elementos maiores que {k}:', len(x[condicao]))
