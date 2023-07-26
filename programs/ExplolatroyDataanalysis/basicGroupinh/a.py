# #
# The "groupby" method groups data by different categories. The data is grouped
# based on one or several variables, and analysis is performed on the individual groups.
#
# For example, let's group by the variable "drive-wheels". We see that there are
# 3 different categories of drive wheels.
#
#



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)

print(df['drive-wheels'].unique())

# Convert the 'price' column to numeric format, handling non-numeric values
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Drop rows with NaN values in the 'price' column
df = df.dropna(subset=['price'])

df_group_one = df[['drive-wheels', 'body-style', 'price']]



df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
print(grouped_test1)
print(df_group_one)




