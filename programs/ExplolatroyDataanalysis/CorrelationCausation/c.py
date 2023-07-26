import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
# Wheel-Base vs. Price

print(df.head())


# Horsepower vs. Price

pearson_co, p_value= stats.pearsonr(df['horsepower'], df['price'])

print("the pearson coeffient is" ,pearson_co, " and the p value is", p_value)