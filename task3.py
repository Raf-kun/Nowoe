import pandas as pd

df = pd.read_csv('Deb.csv')

df_sorted = df.sort_values('ID', ascending=True)
print(df_sorted.head())
