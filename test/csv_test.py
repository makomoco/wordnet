import csv
import numpy as np

# with open("aiueo.csv") as fp:
#     reader = csv.reader(fp)
#     data = [ e for e in reader ]

# data = np.array(data).reshape(-1)

# #以下確認のための出力
# print(data)

with open("aiueo.csv") as fp:
    csvList = list(csv.reader(fp))
flatList = [item for subList in csvList for item in subList]
print(flatList)