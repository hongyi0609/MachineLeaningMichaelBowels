__author__ = "Mike_bowels"
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from random import uniform

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
# read rocks versus mines data into pandas data frame
rocksVMine = pd.read_csv(target_url, header=None, prefix="V")

# change the target to numeric values
target = []
for i in range(208):
    # assign 0 or 1 to target value based on "M" or "R" labels
    if rocksVMine.iat[i, 60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)

# plot 35th attribute
dataRow = rocksVMine.iloc[0:208, 35]
plot.scatter(dataRow, target)

plot.xlabel("Attribute value")
plot.ylabel("Target value")
plot.show()

#
# To improve visualization, this version dithers the points a little and makes them somewhat transparent
target = []
for i in range(208):
    # assign 0 or 1 target values based on "M" or "R" labels and add some dither
    if rocksVMine.iat[i, 60] == "M":
        target.append(1.0 + uniform(-0.1, 0.1))
    else:
        target.append(0.0 + uniform(-0.1, 0.1))

# plot 35th attribute with semi-opaque points
dataRow = rocksVMine.iloc[0:208, 35]
plot.scatter(dataRow, target, alpha=0.5, s=120)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()
