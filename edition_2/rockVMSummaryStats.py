__author__ = 'mike_bowles'
from urllib.request import urlopen
import sys
import numpy as np

# read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
# data = urllib2.urlopen(target_url)
data = urlopen(target_url)

# arrange data to list for labels and list of lists for attributes
xList = []
labels = []

for line in data:
    # split on comma
    row = line.decode('UTF-8').strip().split(",")
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type = [0] * 3
colCounts = []

# generate summary statistics for column 3 (e.g.)
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))

colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)

sys.stdout.write("Mean = " + '\t' + str(colMean) + '\t\t' +
                 "Standard Deviation = " + '\t' + str(colsd) + "\n")

# calculate quantile boundaries
ntitles = 4

percentBdry = []

for i in range(ntitles + 1):
    percentBdry.append(np.percentile(colArray, i * (100) / ntitles))

sys.stdout.write("\nBoundaries for 4 Equal Percentiles \n ")
print(percentBdry)
sys.stdout.write("\n")

# run again with 10 equal intervals
ntitles = 10

percentBdry = []

for i in range(ntitles + 1):
    percentBdry.append(np.percentile(colArray, i * (100) / ntitles))

sys.stdout.write("Boundaries for 10 Equal Percentiles \n")
print(percentBdry)
sys.stdout.write(" \n")

# The last column contains categorical variables

col = 60
colData = []
for row in xList:
    colData.append(row[col])

unique = set(colData)
sys.stdout.write("Unique Label Values \n")
print(unique)

# count up the number of elements having each Values

catDict = dict(zip(list(unique), range(len(unique))))

catCount = [0] * 2

for elt in colData:
    catCount[catDict[elt]] += 1
sys.stdout.write("\n Counts for Each Values of categorical Label \n")
print(list(unique))
print(catCount)
