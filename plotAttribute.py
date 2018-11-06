import numpy as np
import pylab
import scipy.stats as stats
import urllib.request
import sys
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib.request.urlopen(target_url)
xList = []
labels = []
for line in data:
    row = line.strip().split(str.encode(","))
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])
type = [0]*3
colCounts = []
# 分析第4列数据分布情况
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))
stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()