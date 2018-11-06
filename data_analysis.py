import urllib.request
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
type = [0]*3  # 定义一个初始元素为3个0的列表
colCounts = []
for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1  # 是数值
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1  # 非空字符串
            else:
                type[2] += 1  # 内容为空
    colCounts.append(type)
    type = [0]*3
print(" " + '\t' + "Number" + '\t' + "Strings" + '\t ' + "Other")
iCol = 0
for types in colCounts:
    print(str(iCol) + '\t\t' + str(types[0]) + '\t\t' + str(types[1]) + '\t\t' + str(types[2]))
    iCol += 1