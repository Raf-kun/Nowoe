import pandas as pd

df = pd.read_csv('Fake.csv')
x = df[df[source] == "News"]

print(x)
