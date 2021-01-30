from gensim.models.poincare import PoincareModel
from gensim.viz.poincare import poincare_2d_visualization
from IPython import display
from plotly.offline import init_notebook_mode, iplot
import csv
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

init_notebook_mode(connected=True)

# list_from_WordNet_1 学習用のリスト　タプルのリスト
# list_from_WordNet_2 フィルタ用のリスト　一次元リスト
# relations_set プロット用

fig = plt.figure()

# タプル形式で格納
data = pd.read_csv('WordNet_list.csv', header=None)
list_from_WordNet_1 = [(a, b) for a, b in data.values] 
# print(list_from_WordNet_1) #テスト→正常

# モデルの読み込み
model = PoincareModel.load('filename')

# 可視化ツールがset型しか受け付けないので整形
relations_set = set(list_from_WordNet_1)

# ラベルとして可視化する
example_words = ['温度','物性','高温']

# プロット
figure_title = ''
iplot(poincare_2d_visualization(model, relations_set, figure_title, num_nodes=None, show_node_labels=example_words))

fig.savefig("img.png")