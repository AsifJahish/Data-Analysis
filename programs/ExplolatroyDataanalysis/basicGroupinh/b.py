import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)

print(df['drive-wheels'].unique())

df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
print(grouped_test1)

grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
print(grouped_pivot)

grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
print(grouped_pivot)