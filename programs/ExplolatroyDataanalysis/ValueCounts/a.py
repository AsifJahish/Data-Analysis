#
# Value Counts
# Value counts is a good way of understanding how many units of each characteristic/variable we have.
# We can apply the "value_counts" method on the column "drive-wheels". Don’t forget the method "value_counts" only works
# on pandas series, not pandas dataframes. As a result, we only include one bracket df['drive-wheels'],
# not two brackets df[['drive-wheels']].
#
#
#
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = "/home/asifjahish/DataAnalysis/venv/data/automobileEDA.csv"

df = pd.read_csv(filename, header=0)


print(df['drive-wheels'].value_counts())

# We can convert the series to a dataframe as follows:

print(df['drive-wheels'].value_counts().to_frame()
      )


drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
print(drive_wheels_counts)



# Now let's rename the index to 'drive-wheels':
drive_wheels_counts.index.name = 'drive-wheels'
print(drive_wheels_counts)



engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
print(engine_loc_counts.head(10))