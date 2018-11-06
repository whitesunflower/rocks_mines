import urllib.request
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib.request.urlopen(target_url)
xList = []
labels = []
for line in data:
    row = line.strip().split(str.encode(','))
    xList.append(row)
print(xList)
print("Number of Rows of Data = %d " % len(xList))
print("Number of Columns of Data =%d " % len(xList[1]))

