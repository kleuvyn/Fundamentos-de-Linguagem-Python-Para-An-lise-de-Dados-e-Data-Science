import pandas as pd
from pandas import ExcelFile

df = pd.read_csv('/home/kleuvyn/Documentos/MeusRepositorios/Python_Analise_de_Dados_e_Data_Science/temperature.csv')
excel_file: ExcelFile = pd.ExcelFile('/home/kleuvyn/Documentos/MeusRepositorios/Python_Analise_de_Dados_e_Data_Science/temperature.xlsx')
print(df.head())
print('\n', df['date'])
print(type(df['temperatura']))
print('\n', df[['date', 'classification', 'temperatura']])
print(type(df[['date', 'classification']]))
print('\n', df.iloc)
print('\n', df.iloc[:, 1])
print('\n', df.loc)
print('\n', df.loc[:, 'temperatura'])
