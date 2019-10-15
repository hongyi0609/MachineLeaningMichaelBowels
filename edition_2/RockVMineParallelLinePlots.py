__author__ = 'mike_bowels'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# read rocks versus mines data into pandas data frame
rocksVMine = pd.read_csv(target_url, header=None, prefix="V")

for i in range(208):
    # assign color based on "M" or "R" labels
    if rocksVMine.iat[i, 60] == "M":
        pcolor = "red"
    else:
        pcolor = "blue"

    # plot rows of data as if they were series data
    dataRow = rocksVMine.iloc[i,0:60]
    dataRow.plot(color=pcolor)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute value")
plot.title("Rocks vs Mine Parallel Line")
plot.show()