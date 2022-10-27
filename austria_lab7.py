import pandas as pd

df = pd.read_csv("city_temperature.csv", sep = ",") # read in file
grouped_df = df.groupby(['Region']) # group by region and save as new dataframe
idx_max = grouped_df["AvgTemperature"].idxmax() # find rows with max temp values
df = df.loc[idx_max] # return entire rows with max temp values 

# writing out data to a file called city_maxtemp.csv
outfile = "city_maxtemp.csv"
df.to_csv(outfile, index = False)