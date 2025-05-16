import pandas as pd

df = pd.read_csv('Cryptocurrency Transaction Data.csv')
# print(df.describe())
x = df[['Transaction_Fee', 'Gas_Price_Gwei']].nunique()
print(x)
