import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('tittanic2.csv')

# Описательная статистика для числовых столбцов
df.describe()

# Количество пассажиров по классам
sns.boxplot(df['Fare'])
plt.title('Выбросы в Fare')
plt.show()
