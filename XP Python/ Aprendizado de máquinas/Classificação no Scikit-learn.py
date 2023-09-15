import numpy as np
import pandas as pd
from pandas import ExcelFile

df = pd.read_csv('./temperature.csv')
excel_file: ExcelFile = pd.ExcelFile(
    './temperature.xlsx')
print(df, '\n')

# Extração de x e y
x, y =df [['temperatura']].values, df[['classification']].values
print('x:\n', x, '\n')
print('y:\n', y, '\n')

# pre-processamento
from sklearn.preprocessing import LabelEncoder

# conversão de y para valor numerico
codificador = LabelEncoder()
y = codificador.fit_transform(y.ravel())
print('y:\n', y , '\n')

#  modelo
from sklearn.linear_model import LogisticRegression

#Classificador
regresao = LogisticRegression()
regresao.fit(x, y)

# gerando 100 valores de temperatura
# linearmente espacados entre 0 e 45
# predicacao eem novos valores de teperatura

x_newvalor = np.linspace(start=0., stop=45., num=100).reshape(-1, 1)

# predicacao desses valores
y_predificador = regresao.predict(x_newvalor)

# print(y_predificador)

# conversao de y_predicador para valores ordinais
y_predificador = codificador.inverse_transform(y_predificador)

# output
output = {'new_temperatura': x_newvalor.ravel(),
        'new_classificacao': y_predificador.ravel()}
output = pd.DataFrame(output)
output.tail()

# estatistica
output.info()

# estatisticas o
output.describe()

# contagem de valore gerados
output['new_classificacao'].values_counts().plot.bar(figsize=(10, 5), rot =0, title='# de novos valores gerados');
