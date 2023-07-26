import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
# Wheel-Base vs. Price

print(df.head())
#
# Engine-Size vs. Price
pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

# The Pearson Correlation Coefficient is 0.8723351674455185  with a P-value of P = 9.265491622198793e-64

# Since the p-value is
# <
#   0.001, the correlation between engine-size and price is statistically significant, and the linear relationship is very strong (~0.872).

# bore vs price
pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value )

# The Pearson Correlation Coefficient is 0.5431553832626603  with a P-value of P =   8.049189483935315e-17
#
# #
# Conclusion:
# Since the p-value is
# <
#   0.001, the correlation between bore and price is statistically significant, but the linear relationship is only moderate (~0.521).

# We can relate the process for each 'city-mpg' and 'highway-mp
