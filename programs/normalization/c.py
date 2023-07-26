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

median_horsepower = df["horsepower"].median()
df["horsepower"].fillna(median_horsepower, inplace=True)
df["horsepower"] = df["horsepower"].astype(int)

# Plotting the histogram
plt.hist(df["horsepower"])
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)
df[['horsepower', 'horsepower-binned']].head(20)

count = df["horsepower-binned"].value_counts()
print(count)

plt.bar(group_names, df["horsepower-binned"].value_counts())
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()
