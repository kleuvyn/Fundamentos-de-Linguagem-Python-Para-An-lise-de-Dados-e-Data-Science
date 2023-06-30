import numpy as np

x = np.ones((2, 2))
y = np.eye(2)
print("\nx:\n", x)
print("y:\n", y)

print("soma = np.add(x, y)")
print("\nSoma de dois arrays:\n", x + y)
print("Soma com float/int>:\n", x + 2) #broadcasting

print("subtracao = np.subtract(x, y)")
print("\nSubtração de dois arrays:\n", x - y)
print("Subtração com float/int>:\n", x - 2)  #broadcasting

print("divisao = np.divide(x,y)")

#print("\nDivisão de dois arrays:\n", x / y)
#print("Divisão com float/int>:\n", x / 2) #broadcasting

print("multiplicacao = np.multiply(x, y)")
print("\nMultiplicação de dois arrays:\n", x * y)
print("Multiplicação com float/int>:\n", x * 2) #broadcasting

print("Quandoa o broadcasting não funciona \nnp.array([1 ,2 , 3]) + np.array([1, 2]) vai da erro")
print("soma, subtração e divisão")
print('\nCombinação de Operações\n', (x+y)/( x-2))

print("Funções Aritméticas:Multiplicação\nMultiplicação elementos a elementos")
print("\nx:\n", x)
print("\ny:\n", y)

print("multiplicação")
print("\nMultiplicação de dois arrays:\n", x * y)
print("\nMultiplicação com float/int>:\n", x * 2) #broadcasting

print("multiplicação matricial")
print("\nmultiplicaçã matricial (np.dot):\n", np.dot(x, y))
print("\nmultiplicaçã matricial (@):\n", x @ y)
print("\nmultiplicaçã matricial (np.dot):\n", x.dot(y))

print("\nDefinição do problema")
a = np.array([[1, 2], [3, -2]])
c = np.array([[7],[-11]])
print("a:\n", a)
print("\nc:\n", c)

print("\nSolução")
x = np.dot(np.linalg.inv(a), c)
x = np.linalg.inv(a) @ c
print("(a, b)", x.ravel())