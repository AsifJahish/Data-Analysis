import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)
# Wheel-Base vs. Price

print(df.head())
#
# city_mpg vs price
pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# The Pearson Correlation Coefficient is -0.6865710067844678  with a P-value of P =  2.3211320655675098e-29

# conclusion the p_value is less than 0.001 so strong confidance and the pearson correlation coefficient is -0 is less linear correlation

# Conclusion:
# Since the p-value is
# <
#   0.001, the correlation between city-mpg and price is statistically significant,
#   and the coefficient of about -0.687 shows that the relationship is negative and moderately strong.


#  highway_mpg vs price
pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value )

# The Pearson Correlation Coefficient is -0.704692265058953  with a P-value of P =  1.749547114447557e-31

# Conclusion:
# Since the p-value is < 0.001, the correlation between highway-mpg and price is statistically significant,
# and the coefficient of about -0.705 shows that the relationship is negative and moderately strong.