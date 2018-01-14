__author__ = "Mike_bowels"
import sys
from math import sqrt

import pandas as pd

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
# read rocks versus mines data into pandas data frame
rocksVMine = pd.read_csv(target_url, header=None,prefix="V")

#calculate correlations between real-valued attributes
dataColumn2 = rocksVMine.iloc[0:208, 1]
dataColumn3 = rocksVMine.iloc[0:208, 2]
dataColumn21 = rocksVMine.iloc[0:208, 20]

mean2 = 0.0; mean3 = 0.0; mean21 = 0.0
numElt = len(dataColumn2)
for i in range(numElt):
    mean2 += dataColumn2[i] / numElt
    mean3 += dataColumn3[i] / numElt
    mean21 += dataColumn21[i] / numElt

var2 = 0.0;var3 = 0.0;var21 = 0.0
for i in range(numElt):
    var2 += (dataColumn2[i] - mean2) * (dataColumn2[i] - mean2) / numElt
    var3 += (dataColumn3[i] - mean3) * (dataColumn3[i] - mean3) / numElt
    var21 += (dataColumn21[i] - mean21) * (dataColumn21[i] - mean21) / numElt

corr23 = 0.0; corr221 = 0.0
for i in range(numElt):
    corr23 = (dataColumn2[i] - mean2) * \
             (dataColumn3[i] - mean3) / (sqrt(var2 * var3) * numElt)
    corr221 = (dataColumn2[i] - mean2) * \
              (dataColumn21[i] - mean21) / (sqrt(var2 * var21) * numElt)

sys.stdout.write("Correlation between attribute 2 and 3 \n")
print(corr23)
sys.stdout.write(" \n")
sys.stdout.write("Correlation between attribute 2 and 21 \n")
print(corr221)