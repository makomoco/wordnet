import pandas as pd

data = pd.read_csv('aiueo.csv', header=None)
list_csv = [(a,b) for a,b in data.values]

print(list_csv)