# Correlation: a measure of the extent of interdependence between variables.
#
# Causation: the relationship between cause and effect between two variables.
#
# It is important to know the difference between these two. Correlation does not imply causation.
# Determining correlation is much simpler the determining causation as causation may require independent experimentation.



# Pearson Correlation
#
# The Pearson Correlation measures the linear dependence between two variables X and Y.
#
# The resulting coefficient is a value between -1 and 1 inclusive, where:
#
# 1: Perfect positive linear correlation.
# 0: No linear correlation, the two variables most likely do not affect each other.
# -1: Perfect negative linear correlation.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# from scipy import stats

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)



grouped_price_by_body_style = df.groupby('body-style')['price'].mean()

print(grouped_price_by_body_style)

print(df.head())

print(df.isnull().sum())

print(df.dtypes)

# correlation

df = df.drop(columns=['body-style'])

# # Option 1: Convert to categorical data type
# df['body-style'] = df['body-style'].astype('category')

# Option 2: One-hot encoding
df = pd.get_dummies(df, columns=['body-style'], drop_first=True)


# Print the data types of each column
print(df.dtypes)

# Check for any columns with non-numeric data
non_numeric_columns = df.select_dtypes(exclude=['float64', 'int64']).columns
print("Non-Numeric Columns:", non_numeric_columns)

# Drop non-numeric columns from the DataFrame
df = df.drop(columns=non_numeric_columns)

# Calculate the correlation matrix
print(df.corr())


