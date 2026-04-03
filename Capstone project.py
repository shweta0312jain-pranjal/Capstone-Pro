import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Penguins Data.csv")

print(data.head())

print(data.isnull().sum())

sns.heatmap(data.isnull())
plt.show()

data = data.fillna(data.mean(numeric_only=True))

data = data.fillna(data.mode().iloc[0])

sns.pairplot(data)
plt.show()

sns.heatmap(data.corr(numeric_only=True))
plt.show()

data.plot(kind='box')
plt.show()

sns.countplot(x='Gender', data=data)
plt.show()