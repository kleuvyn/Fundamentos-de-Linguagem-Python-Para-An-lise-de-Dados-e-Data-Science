import pandas as pd
from pandas import ExcelFile

df = pd.read_csv('/temperature.csv')
excel_file: ExcelFile = pd.ExcelFile('/temperature.xlsx')
print(df.head())
print('\n', df['date'])
print(type(df['temperatura']))
print('\n', df[['date', 'classification', 'temperatura']])
print(type(df[['date', 'classification']]))
print('\n', df.iloc)
print('\n', df.iloc[:, 1])
print('\n', df.loc)
print('\n', df.loc[:, 'temperatura'])
