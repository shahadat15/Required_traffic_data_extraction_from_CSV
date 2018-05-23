
import pandas as pd
import numpy as np

a = pd.read_csv("U:\PDF2Table\Input_data.csv",header = None)
month_ = input("What is Month name? ")

p1 = np.empty((24,15))
p1[:] = 0
p1 = pd.DataFrame(p1)
for i in range(0,24):
    p1[7][i] = i;
i=0
j=0
for row in a.iterrows():
    if (not(pd.isna(row[1][0]))):
        if (row[1][0].isnumeric()):
            p1[j][i]= row[1][7]
            p1[(j+8)][i] = row[1][14]
            i = i + 1
            #p1.append([row[1][7],row[1][14]])
        elif ((row[1][0] == month_)& (row[1][3] != "All")):
            p1[j][i]= row[1][10]
            p1[(j+8)][i] = row[1][17]
            i=i+1
            #p1.append([row[1][10], row[1][17]])
        elif ((row[1][0] == "All")|(row[1][3] == "All")):
            i = 0
            j = j + 1
            if (j>6): break

p1.to_csv("U:\PDF2Table\Output_data.csv",header=None, index=None)