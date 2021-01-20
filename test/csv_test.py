import csv
import numpy as np

with open("aiueo.csv") as fp:
    csvList = list(csv.reader(fp))
flatList = [item for subList in csvList for item in subList]
print(flatList)

list_2 = ['あ','は']

ls = [l for l in list_2 if l in flatList] 

print(ls)