import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = pd.read_csv(target_url, header=None, prefix="V")
dataRow2 = data.iloc[0:208, 1]
dataRow3 = data.iloc[0:208, 1]

plot.scatter(dataRow2, dataRow3)
plot.xlabel("2nd Attribute")
plot.ylabel("3rd Attribute")
plot.show()

dataRow21 = data.iloc[0:208, 20]
plot.scatter(dataRow2, dataRow21)
plot.xlabel("2nd Attribute")
plot.ylabel("21st Attribute")
plot.show()