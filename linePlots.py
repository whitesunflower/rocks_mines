import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")
num = rocksVMines.shape[0]
for i in range(num):
    if rocksVMines.iat[i, 60] == "M":
        pcolor = "red"
    else:
        pcolor = "green"
    dataRow = rocksVMines.iloc[i, 0:60]
    dataRow.plot(color=pcolor, alpha=0.5)
plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()
