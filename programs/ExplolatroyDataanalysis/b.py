import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
print(df.head())

print(df.dtypes)

print(df['peak-rpm'].dtypes)


df = df.fillna(np.nan)



df = df.apply(pd.to_numeric, errors='coerce')


correlation_matrix = df.corr()
print(correlation_matrix)

correlation= df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()

print(correlation)
