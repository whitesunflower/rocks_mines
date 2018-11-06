import pandas as pd
from pandas import DataFrame
from math import sqrt
import sys
# 计算属性之间的皮尔逊相关系数


target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = pd.read_csv(target_url, header=None, prefix="V")
dataRow2 = data.iloc[:, 1]
dataRow3 = data.iloc[:, 2]
dataRow21 = data.iloc[:, 20]
mean2 = 0.0
mean3 = 0.0
mean21 = 0.0
numElt = data.shape[0]
for i in range(numElt):
    mean2 += dataRow2[i]/numElt
    mean3 += dataRow3[i]/numElt
    mean21 += dataRow21[i]/numElt
var2 = 0.0
var3 = 0.0
var21 = 0.0
for i in range(numElt):
    var2 += (dataRow2[i] - mean2) * (dataRow2[i] - mean2)
    var3 += (dataRow3[i] - mean3) * (dataRow3[i] - mean3)
    var21 += (dataRow21[i] - mean21) * (dataRow21[i] - mean21)

corr23 = 0.0
corr221 = 0.0
for i in range(numElt):
    corr23 += (dataRow2[i] - mean2) * (dataRow3[i] - mean3) / sqrt(var2*var3)
    corr221 += (dataRow2[i] - mean2) * (dataRow21[i] - mean21) / sqrt(var2*var21)
print("Correlation between attribute 2 and 3 : %f" % corr23)
print("Correlation between attribute 2 and 21 : %f " % corr221)
