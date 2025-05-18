import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('tittanic2.csv')

# Распределение возрастов по классам
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Age по классам')
plt.show()
