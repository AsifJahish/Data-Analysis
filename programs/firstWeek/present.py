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

# to see To see which values are present in a particular column, we can use the ".value_counts()" method:
value= df['num-of-doors'].value_counts()
#We can see that four doors are the
# most common type. We can also use the ".idxmax()" method to calculate the most common type automatically:
common=df['num-of-doors'].value_counts().idxmax()

print(df[df[
"num-of-doors"
].isnull()])

df["num-of-doors"].replace(np.nan, common, inplace=True)



print("the most common: " + str(common))
print("all the values that exist with how many times they occur:\n" + str(value))
print(df.head())
