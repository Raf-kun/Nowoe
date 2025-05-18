import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tittanic2.csv')

# Соотношение выживших/погибших
df['Survived'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Соотношение выживших и погибших')
plt.ylabel('')
plt.show()
