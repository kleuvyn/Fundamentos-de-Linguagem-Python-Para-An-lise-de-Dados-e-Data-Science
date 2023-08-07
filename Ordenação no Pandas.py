import pandas as pd
from pandas import ExcelFile

df = pd.read_csv('/home/kleuvyn/Documentos/MeusRepositorios/Python_Analise_de_Dados_e_Data_Science/temperature.csv')
excel_file: ExcelFile = pd.ExcelFile(
    '/home/kleuvyn/Documentos/MeusRepositorios/Python_Analise_de_Dados_e_Data_Science/temperature.xlsx')

print('\n01\n', df.sort_values)
print('\n02 Ordenação crescente por coluna\n', df.sort_values(by='temperatura'))
print('\n03\n Ordenação decrescente por coluna', df.sort_values(by='temperatura', ascending=False))
print('\n04 Ordenação crescente por coluna\n', df.sort_values(by='classification'))
print('\n05 Ordenação crescente por coluna\n', df.sort_values(by=['classification', 'temperatura']))
print('\n06 Ordenação crescente por coluna\n', df.sort_index())
print('\n07 Ordenação decrescente por coluna\n', df.sort_index(ascending=False))
print('\n08.\n', df.groupby(by='classification').mean('classification'))
print('\n09.\n', df.groupby(by='classification').sum('classification'))
print('\n10.\n', df.drop('temperatura', axis=1))