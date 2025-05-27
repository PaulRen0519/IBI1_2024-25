import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# the basic functions of os library
os.chdir("Practical10")
# other useful funcitons in os:
    # os.getcwd()
    # os.listdir()

# practice the iloc function to pick the columns and rows
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.describe())

# show the first 10 rows
print(dalys_data.head(10))
# result turns out that the 10th year in Afghanistan DALYs is 82624.94

# other useful functions:
    # dalys_data.iloc[2,0:5]
    # dalys_data.iloc[0:10:2,0:5]

# first three rows, but only the first, second, and fourth column, using Boolean:
    # my_columns = [True, True, False, True]
    # dalys_data.iloc[0:3,my_columns]
    # or dalys_data.iloc[0:3,[0,1,3]]

# select and print the rows whose year is 1990
dalys_data.loc[2:4, "Year"]
check_1990 = dalys_data["Year"] == 1990
print(dalys_data.loc[check_1990,[True, True, False, True]])

# comopare the mean dalys of the UK and France
uk = dalys_data.loc[dalys_data.Entity == 'United Kingdom', ["DALYs", "Year"]]
fr = dalys_data.loc[dalys_data.Entity == 'France', ["DALYs", "Year"]]
uk_mean = uk["DALYs"].mean()
fr_mean = fr["DALYs"].mean()
print(f"mean DALYs of the UK: {uk_mean}\nmean DALYs of France: {fr_mean}")

if uk_mean > fr_mean:
    print("Mean DALYs in the UK was greater than France.")
elif uk_mean < fr_mean:
    print("Mean DALYs in the UK was smaller than France.")
else:
    print("Mean DALYs in the UK was equal to that in France.")

plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year, rotation = -90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("UK's DALYs")
plt.show()

# solve another quesiton of which countries's DALYs is greater than 88000 in 1990
row_1990 = dalys_data.loc[check_1990,[True, True, False, True]]
sel_row = row_1990[dalys_data["DALYs"] > 88000]
print(sel_row[['Entity','DALYs']])
plt.bar(sel_row["Entity"], sel_row["DALYs"])
plt.xticks(sel_row["Entity"], rotation = -90)
plt.xlabel("Countries")
plt.ylabel("DALYs")
plt.title("Contries with DALYs larger than 88000 in 1990")
plt.show()