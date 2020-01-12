import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('single_family_home_values.csv')
df.dropna(inplace=True)
df=df[df.estimated_value<=1000000]
df=df[df.lastSaleAmount<=1000000]
#sns.boxplot(df.estimated_value)
#sns.pairplot(df[['lastSaleAmount', 'estimated_value', 'zipcode']])
#sns.stripplot(x=df.zipcode, y=df.estimated_value)
sns.violinplot(x=df.zipcode, y=df.estimated_value)
df['priorSaleDate'] = pd.to_datetime(df.priorSaleDate)
df['lastSaleDate'] = pd.to_datetime(df.lastSaleDate)

plt.show()