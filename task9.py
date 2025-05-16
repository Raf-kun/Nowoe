import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('tittanic2.csv')

# Тепловая карта корреляций
corr_matrix = df[['Age', 'Fare', 'SibSp', 'Parch']].corr()
sns.heatmap(corr_matrix, annot=True)
plt.title('Корреляции числовых признаков')
plt.show()

# Связь возраста и цены билета (scatter plot)
sns.scatterplot(x='Age', y='Fare', data=df)
plt.title('Age vs Fare')
plt.show()
