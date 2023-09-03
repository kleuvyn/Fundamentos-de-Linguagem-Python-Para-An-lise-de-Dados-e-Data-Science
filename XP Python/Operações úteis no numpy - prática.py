import numpy as np

x = np.array([[1, 3, 7], [4, 11, 21], [42, 8, 9]])
print('x:\n', x)
print('\n*Reshspe:tranforma a matrix em um vetor coluna/linha')
print('Transformação de em vetor linha:\n', x.reshape((1, 9)))
print('Transformação de em vetor coluna:\n', x.reshape((9, 1)))
print('\nTransposição de matrix:\n', x.T)
print('\nnp.sum: soma em um dado eixo, axis = {0 : linha, 1 ; coluna}')
print('Soma de todos alementos de x:', np.sum(x))
print('Soma de x ao longo das linhas:', np.sum(x, axis=0))
print('Soma de x ao longo das colunas:', np.sum(x, axis=1))
print('\nnp.mean:Média em um dado eixo, axis = {0 : linha, 1 ; coluna}')
print('Média de todos alementos de x:', np.mean(x))
print('Média de x ao longo das linhas:', np.mean(x, axis=0))
print('Média de x ao longo das colunas:', np.mean(x, axis=1))
print('\nnp.wherw, identificação dos índicees onde uma dada condição'
      'é atendida .Uso conjunto com indexação booleana')
print('Numeros pares')
cond = x % 2 == 0
print('Condição:\n', cond)
print('\nÍndices x[i, j] = x=[cond]')
i, j = np.where(cond)
print('Índice i [linhas]:', i)
print('Índice j [colunas]', j)
print('\nIndexação booleana e slicing:selecionar as linhas de x que possuem número par ')
print('Números pares')
print('x:\n', x)
cond = x % 2 == 0
print('Condição:\n', cond)
print('\nSe ouver alguma condição True na Linha, a Soma será > 0')
i_row = np.where(np.sum(cond, axis=1))[0]
print('Índice das linhas que possuem números pares:', i_row)
print('Linhas que possuem números pares:\n', x[i_row, :])
