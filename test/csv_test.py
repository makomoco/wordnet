import csv
import numpy as np

with open("aiueo.csv") as fp:
    reader = csv.reader(fp)
    data = [ e for e in reader ]

data = np.array(data).reshape(-1)

#以下確認のための出力
print(data)