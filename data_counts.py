# -*- coding:utf-8 -*-
import urllib.request
import sys
import numpy as np

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
# 以col = 3这一列为例
# 求这一列数据的平均值和标准差
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))
colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)
print("Mean = %d ， std = %d" % (colMean, colsd))
# 求这一列数据的百分位数
ntiles = 4
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
print("0分位数为：%f" % percentBdry[0])
print("4分之1分位数为：%f" % percentBdry[1])
print("中位数为：%f" % percentBdry[2])
print("4分之3分位数为：%f" % percentBdry[3])
print("1分位数为：%f" % percentBdry[4])
# 输出第60列数据的唯一值
col = 60
colData = []
for row in xList:
    colData.append(bytes.decode(row[col]))
unique = np.unique(colData)
print("Unique Label Values：")
print(list(unique))
catDict = dict(zip(list(unique), range(len(unique))))
# 统计唯一值各有多少个
catCount = [0]*2
for elt in colData:
    catCount[catDict[elt]] += 1
print(catCount)