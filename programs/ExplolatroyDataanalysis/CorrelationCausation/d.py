import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
# Wheel-Base vs. Price

print(df.head())
#
# Length vs. Price

pearson_co, p_value= stats.pearsonr(df['length'], df['price'])
print("the pearson coeffient is ", pearson_co, " and the p_value is ", p_value)


# the pearson coeffient is  0.6906283804483639  and the p_value is  8.01647746615924e-30



pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value )


# The Pearson Correlation Coefficient is 0.7512653440522675  with a P-value of P = 9.200335510480491e-38