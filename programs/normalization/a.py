import pandas as pd
import numpy as np

# Provide the correct file path for your CSV file
file_path = "/home/asifjahish/DataAnalysis/venv/data/auto.csv"

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(file_path, names=headers)
df.replace("?", np.nan, inplace = True)
missing_data = df.isnull()


df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
median_value = df["normalized-losses"].median()
df["normalized-losses"].fillna(median_value, inplace=True)
df[["normalized-losses"]] = df[["normalized-losses"]].astype(int)
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
df[["price"]] = df[["price"]].astype("float")

# # Convert mpg to L/100km by mathematical operation (235 divided by mpg)
# df['city-L/100km'] = 235/df["city-mpg"]

# check your transformed data
df.head()
print(df.head())

df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()

print(df.head())