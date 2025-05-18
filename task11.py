import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('tittanic2.csv')

# Описательная статистика для числовых столбцов
df.describe()

# Количество пассажиров по классам
sns.countplot(x='Pclass', data=df)
plt.title('Количество пассажиров по классам')
plt.show()
