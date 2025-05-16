import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('titanic.csv')
pd.crosstab(df['Sex'], df['2urvived'])

# Гистограмма возрастов
df['Age'].hist(bins=20)
plt.title('Распределение возрастов')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Boxplot цен билетов для выживших и погибших
import seaborn as sns
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Fare vs Survived')
plt.show()