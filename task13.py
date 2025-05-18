import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('tittanic2.csv')

# Age vs Fare
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title('Age vs Fare (с учетом выживаемости)')
plt.show()
