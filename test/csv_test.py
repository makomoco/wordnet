import pandas as pd

data = pd.read_csv('aiueo.csv', header=None)
list_csv = [l for l in data.values]

print(list_csv)