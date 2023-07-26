import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)


# Use the "groupby" function to find the average "price" of each car based on "body-style".


grouped_price_by_body_style = df.groupby('body-style')['price'].mean()

print(grouped_price_by_body_style)
