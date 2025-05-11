import pandas as pd

df = pd.read_csv('Deb.csv')

print(df.isnull().sum)
