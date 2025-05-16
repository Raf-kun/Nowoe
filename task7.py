import pandas as pd

df = pd.read_csv('titanic.csv')
pd.crosstab(df['Sex'], df['2urvived'])

x = df.groupby('Pclass')['2urvived'].mean() * 100
print(x)
