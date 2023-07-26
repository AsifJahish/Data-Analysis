


#
#
# What is an indicator variable?
# An indicator variable (or dummy variable) is a numerical variable used to label categories. They are called 'dummies' because the numbers themselves don't have inherent meaning.
#
# Why we use indicator variables?
# We use indicator variables so we can use categorical variables for regression analysis in the later modules.







import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

# Provide the correct file path for your CSV file
file_path = "/home/asifjahish/DataAnalysis/venv/data/auto.csv"

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(file_path, names=headers)
df.replace("?", np.nan, inplace=True)
missing_data = df.isnull()


print( df.columns)


dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.head()

print(dummy_variable_1.head())


dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
print(dummy_variable_1.head())

# merge data frame "df" and "dummy_variable_1"
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)

print(df.head())

df.to_csv('clean_df.csv')