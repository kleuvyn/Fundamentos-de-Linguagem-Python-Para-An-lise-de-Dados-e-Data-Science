import numpy as np
#Array 1D
#help(np.array)

lista = [1, 2, 3]
x = np.array(lista)
print("\nx:\n", x)
print ("shape:", x.shape )

#Array 2D
lista = [[1, 2], [3,4]]
x = np.array(lista)
print("\nx:\n", x)
print("shape:", x.shape)

#Array contendo apenas 0
dim = (4, 4) #(linhas, colunas)
x = np.zeros(dim)
print("\nx:\n", x)
print("shape:", x.shape)

size = (12, 12) #(linhas, colunas)
x = np.ones(size)
print("\nx:\n", x)
print("shape:", x.shape)

#valores dentro de intervaloe, valores iniformes entre 5 e 15
xmin, xmax = 5, 15
x =  np.linspace(start= xmin, stop=xmax, num=6)
print("\nx:\n", x)
print("shape:", x.shape)

#matrix identidade
n = 4
x =  np.eye(n)
print("\nx:\n", x)
print("shape:", x.shape)

#valores aleatórios
x =  np.random.random(size=(2, 3))
print("\nx:\n", x)
print("shape:", x.shape)

#Indentação
x = np.linspace(start=10, stop=100, num=10)
print("\nx:\n", x)
print("shape:", x.shape)

#extração de elementos
x = np.linspace(start=10, stop=100, num=10)
print("\nx:", x)
print("\nPrimeiro elemento:", x[0])
print("\nSegundo elemento:", x[1])
print("\nÚltimo elemento:", x[9])
print("\nÚltimo elemento:", x[-1])

#Slincing extraão de subarrays
x = np.linspace(start=10, stop=100, num=10)
print("\nx:", x)
print("\nDois primeiros elemento:", x[0:2])
print("\nDois primeiros elemento:", x[:2])
print("\nDois últimos elemento:", x[-2:])

#slicing extração de arrauys 2d
x = x.reshape(2, 5)
print("\nx:\n", x)

#extração de elementos
print("\nx:", x)
print("\nPrimeiro elemento:", x[0, 1])
print("\nSegundo elemento:", x[1, -2])
print("\nÚltimo elemento:", x[1,4])
print("\nÚltimo elemento:", x[-1, -1])

#slicine estração subarrays
print("\nx:", x)
print("\nPrimeira linha interia:", x[0, :])
print("\nPrimeira á Quarta linha:", x[0, 1:4])
print("\nÚltima linha:\n", x[:, [-1]])

#compartilhamento de subarrays y altera o valor de x
x = np.array([1, 2, 3])
print("\nx antes:", x)
y = x[:2]
y[0] = -100
print("x depois:", x)

#compartilhamento de subarrays y não altera o valor de x
x = np.array([ 1, 2, 3])
print("\nx antes:", x)
y = x[:2].copy()
y[0] = -100
print("x depois:", x)


