import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
print(df.head())


sns.regplot(x="stroke", y="price", data=df)
plt.show()

correlation=df[["stroke","price"]].corr()

print(correlation)