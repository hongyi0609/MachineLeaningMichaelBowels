__author__ = 'Mike Bowles'
import numpy as np
import pylab
import scipy.stats as stats
from urllib.request  import urlopen

target_url =  ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urlopen(target_url)

# arrange data into list for labels and list of lists for attributes
xList = []
labels = []

for line in data:
    # split on comma
    row = line.decode('UTF-8').strip().split(",")
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])
type = [0]*3
colCounts = []

# generate summary statistics for columns 3 (e.g.)
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))

stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()