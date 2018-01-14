__author__ = 'mike_bowels'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
# read rocks versus mines data into pandas data frame
rocksVMine = pd.read_csv(target_url, header=None,prefix="V")

# calculate correlations between real-valued attributes
dataRow2 = rocksVMine.iloc[1,0:60]
dataRow3 = rocksVMine.iloc[2,0:60]

plot.scatter(dataRow2, dataRow3)

plot.xlabel("2nd Attribute")
plot.ylabel("3rd Attribute")
plot.show()

dataRow21 = rocksVMine.iloc[20, 0:60]
plot.scatter(dataRow2, dataRow21)

plot.xlabel("2nd Attribute")
plot.ylabel("21st Attributes")
plot.show()