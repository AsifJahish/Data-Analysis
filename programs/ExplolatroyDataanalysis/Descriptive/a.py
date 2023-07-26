# Descriptive Statistical Analysis¶
# Let's first take a look at the variables by utilizing a description method.
#
# The describe function automatically
# computes basic statistics for all continuous variables.
# Any NaN values are automatically skipped in these statistics.
#
# This will show:
#
# the count of that variable
# the mean
# the standard deviation (std)
# the minimum value
# the IQR (Interquartile Range: 25%, 50% and 75%)
# the maximum value







import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
print(df.head())

print(df.describe())


print(df.describe(include=['object']))
