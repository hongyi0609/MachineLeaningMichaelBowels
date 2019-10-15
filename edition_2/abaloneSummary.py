__author__ = 'mike_bowles'

import pylab
import matplotlib.pyplot as plot

import pandas as pd
from pandas import DataFrame

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/"
              "abalone/abalone.data")
# read abalone data
abalone = pd.read_csv(target_url, header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole Weight',
                   'Shucked Weight', 'Viscera Weight', 'Shell Weight', 'Rings']
print(abalone.head())
print(abalone.tail())

#print summary of data frame
summary = abalone.describe()
print(summary)

#box plot the real-valued attributes convert to array for plot routine
array = abalone.iloc[:, 1:9].values
boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")
show()

# the last column (Rings) is out of scale with the rest - remove and replot
arrays2 = abalone.iloc[:,1:8].values
boxplot(arrays2)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")
show()

# removing is okay but renormalizing the variables generalizes better.
# renormalize columns to zero mean and unit standard deviation
# this is a common normalization and desirable for other operations
# (like k-means clustering(K均值聚类) or k-nearest neighbors)
abaloneNormalized = abalone.iloc[:,1:9]

for i in range(8):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2,i]
    abaloneNormalized.iloc[:,i:(i+1)] = (abaloneNormalized.iloc[:,i:(i+1)] - mean) / sd

array3 = abaloneNormalized.values
boxplot(array3)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges - Normalized ")
show()