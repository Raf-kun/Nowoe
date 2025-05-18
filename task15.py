import pandas as pd
# import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
df_sorted = df.sort_values('Sale_Date', ascending=False)
df_sorted.head()
# df.set_index('Sale_Date')['Sales_Rep'].plot()
# plt.title('Динамика продаж')
# plt.show()
print(df_sorted.head(10))
