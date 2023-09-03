import pandas as pd
from pandas import ExcelFile

df = pd.read_csv('/temperature.csv')
print(df)

excel_file: ExcelFile = pd.ExcelFile('/temperature.xlsx')
df2 = pd.read_excel(excel_file, sheet_name='Sheet1')
print('\n', excel_file)
print('\n', df2)

df3 = pd.read_excel(excel_file, sheet_name='Sheet2', decimal=',')
df3 = pd.read_excel(excel_file, sheet_name='Sheet2')
print('\n', excel_file)
print('\n', df3)

n = 3
print('\n', df.head(n))
print('\n', df.tail(n))
print('\n', df.dtypes)
print('\n', df.describe(), '\n')
print('\n', df.info())
print('\n', df.columns)

