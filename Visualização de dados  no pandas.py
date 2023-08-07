import pandas as pd
from pandas import ExcelFile
import matplotlib.pyplot as plt


df = pd.read_csv('/home/kleuvyn/Documentos/MeusRepositorios/Python_Analise_de_Dados_e_Data_Science/temperature.csv')
excel_file: ExcelFile = pd.ExcelFile(
    '/home/kleuvyn/Documentos/MeusRepositorios/Python_Analise_de_Dados_e_Data_Science/temperature.xlsx')

# df.plot();
# print('\n02.plot linhas: tamanho', df.plot(figsize=(10, 5)))
# print('\n03.plot linhas: grid', df.plot(figsize=(10, 5), grid=True))
# print('\n04.plot linhas: slyle', df.plot(style='-o',figsize=(10, 5), grid=True))
# print('\n05.plot linhas: slyle', df.plot(style='--',figsize=(10, 5), grid=True))
# print('\n06.plot linhas: slyle', df.plot(style='-.',figsize=(10, 5), grid=True))
# print('\n07.plot linhas: linewidth', df.plot(style='-o', linewidth=2.5, figsize=(10, 5), grid=True))
# print('\n08.plot linhas: color', df.plot(style='-o', linewidth=2.5, color='red', figsize=(10, 5), grid=True))
# print('\n09.plot linhas: color', df.plot(style='-o', linewidth=2.5, color='#b05dcf', figsize=(10, 5), grid=True))
# print('\n10.plot de barras', df.plot(kind='bar', figsize=(10, 5), rot=30));
# print('\n11.plot de barras', df['classification'].value_counts().plot.bar(figsize=(10, 5), rot=0));
# print('\n11.plot pizza', df['classification'].value_counts().plot.pie(autopct= '%1.1f%%', shadow=True, figsize=(10, 5)));
# print('\n08 agrupamento po valores úbicos de uma ou mais colunas\n', df.groupby(by='classification'))
plt.show()