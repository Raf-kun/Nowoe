import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('tittanic2.csv')

# Boxplot для поиска выбросов в 'Fare'
sns.boxplot(df['Fare'])
plt.title('Выбросы в Fare')
plt.show()

# Удаление строк, где Fare > 300 (аномалии)
df = df[df['Fare'] <= 300]
