import pandas as pd
import numpy as np


df = pd.read_csv("/home/asifjahish/DataAnalysis/venv/student.csv", header=None)

print("The first 5 rows of the dataframe")
first = df.head(5)
df1 = df.replace('?', np.NaN)

des= df1.describe(include="all")

onlydes= df.describe()
print(des)

print("to describe the first data ")

print(onlydes)
