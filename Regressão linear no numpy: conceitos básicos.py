import matplotlib.pyplot as plt
import numpy as np
#
x = [-1., -0.77777778, -0.5555556, -0.3333333, -0.1111111,
      0.1111111, 0.3333333, 0.5555556, 0.7777778, 1.]
y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49405657,
     1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

print('Plot dos dados')
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='Dados Originais')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

print('\nPlot dos dados')
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Dados Originais')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

Transformando para numpy e vetor coluna'
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)
# Adicioando bias: para estimar o termo b
x = np.hstack((x, np.ones(x.shape)))
# estimando a e b
beta = np.linalg.pinv(x).dot(y)
print('a estimado:', beta[0][0])
print('b estimado:', beta[1][0])

print('\nPlot dos dados')
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='Dados Originais')
plt.plot(x, x.dot(beta), label='Regressão Linear')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão Linear com Numpy')
plt.grid()
plt.show()
