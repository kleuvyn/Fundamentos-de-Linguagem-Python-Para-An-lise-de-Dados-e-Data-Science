import pandas as pd
from pandas import ExcelFile

df = pd.read_csv('/temperature.csv')
excel_file: ExcelFile = pd.ExcelFile(
    '/temperature.xlsx')

print(df.dtypes)
df['date'] = pd.to_datetime(df['date'])
print('\n1',df.dtypes)
print('\n3', df.head())
print('\n4', df[df['temperatura'] >= 25])
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
print('\n5', df[df.index <= '2020-03-01'])
print('\n6', df.loc[df.index <= '2020-03-01', ['classification']])
print('\n7', df.iloc[df.index <= '2020-03-01', [-1]])