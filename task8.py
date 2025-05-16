import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('tittanic2.csv')

# Гистограмма возрастов

df['Age'].hist(bins=20)
plt.title('Распределение возрастов')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Boxplot цен билетов для выживших и погибших

sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Fare vs Survived')
plt.show()
