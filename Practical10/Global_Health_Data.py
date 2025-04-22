import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("Practical10")
# os.getcwd()
# os.listdir()

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.describe())
# dalys_data.iloc[0,3]
# dalys_data.iloc[2,0:5]
# dalys_data.iloc[0:10:2,0:5]

# first three rows, but only the first, second, and fourth column, using Boolean
# dalys_data.iloc[0:3,[0,1,3]]

# my_columns = [True, True, False, True]
# dalys_data.iloc[0:3,my_columns]

# select and print the rows whose year is 1990
dalys_data.loc[2:4, "Year"]
check_1990 = dalys_data["Year"] == 1990
print(dalys_data.loc[check_1990,"DALYs"])