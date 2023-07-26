# Binning
# Why binning?
# Binning is a process of transforming continuous numerical
# variables into discrete categorical 'bins' for grouped analysis.
#
# Example:
#
# In our dataset, "horsepower" is a real valued variable ranging
# from 48 to 288 and it has 59 unique values. What if we only care about the
# price difference between cars with high horsepower, medium horsepower,
# and little horsepower (3 types)? Can we rearrange them into three ‘bins' to simplify analysis?
#
# We will use the pandas method 'cut' to segment the 'horsepower' column into 3 bins.


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

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
median_value = df["normalized-losses"].median()
df["normalized-losses"].fillna(median_value, inplace=True)
df[["normalized-losses"]] = df[["normalized-losses"]].astype(int)
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
df[["price"]] = df[["price"]].astype("float")

df['length'] = df['length'] / df['length'].max()
df['width'] = df['width'] / df['width'].max()

median_horsepower = df["horsepower"].median()
df["horsepower"].fillna(median_horsepower, inplace=True)
df["horsepower"] = df["horsepower"].astype(int)

# Plotting the histogram
plt.hist(df["horsepower"])
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins

group_names = ['Low', 'Medium', 'High']

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)

df["horsepower-binned"].value_counts()
count= df["horsepower-binned"].value_counts()
print(count)

import matplotlib as plt
from matplotlib import pyplot
pyplot.bar(group_names, df["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
plt.show()
