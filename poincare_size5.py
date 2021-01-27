from gensim.models.poincare import PoincareModel
from gensim.viz.poincare import poincare_2d_visualization
from IPython import display
from plotly.offline import init_notebook_mode, iplot
import csv
import pandas as pd

init_notebook_mode(connected=True)

##############################################
# 5次元でのモデル作成
##############################################

# list_from_WordNet_1 学習用のリスト　タプルのリスト
# list_from_WordNet_2 フィルタ用のリスト　一次元リスト

# タプル形式で格納
data = pd.read_csv('WordNet_list.csv', header=None)
list_from_WordNet_1 = [(a, b) for a, b in data.values] 
# print(list_from_WordNet_1) #テスト→正常

# WordNet_list.csvを一次元配列（リスト）に格納
with open("WordNet_list.csv") as fp:
    csvList = list(csv.reader(fp))
list_from_WordNet_2 = [item for subList in csvList for item in subList]
# print(list_from_WordNet_2) #テスト→正常


# ポアンカレ埋め込み学習(可視化するため２次元で学習を行う)
model = PoincareModel(list_from_WordNet_1, size=5, negative=8)
model.train(epochs=5000)
model.save('filename_5')