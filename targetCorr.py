import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from random import uniform

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = pd.read_csv(target_url, header=None, prefix="V")
# M标记为1，R标记为0
target = []
for i in range(208):
    if data.iat[i, 60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)
dataRow35 = data.iloc[0:208, 34]
plot.scatter(dataRow35, target)
plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()

target = []
for i in range(208):
    if data.iat[i,60] == "M":
        target.append(1.0 + uniform(-0.1, 0.1))
    else:
        target.append(0.0 + uniform(-0.1, 0.1))
dataRow35 = data.iloc[0:208, 34]
plot.scatter(dataRow35, target, alpha=0.5, s=120)
plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()