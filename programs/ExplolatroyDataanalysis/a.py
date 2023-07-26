import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
print(df.head())

a = list(df["make"])
b = list(df["drive-wheels"])

plt.plot(a, b)

plt.xlabel("Car Company")
plt.ylabel(b)

plt.title("make and drive wheel")

print(df.dtypes)

plt.show()
