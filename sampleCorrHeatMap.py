import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = pd.read_csv(target_url, header=None, prefix="V")
corMat = DataFrame(data.corr())
plot.pcolor(corMat)
plot.show()
