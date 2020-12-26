from gensim.models.poincare import PoincareModel
from gensim.viz.poincare import poincare_2d_visualization
from IPython import display
from plotly.offline import init_notebook_mode, iplot
import pandas as pd

init_notebook_mode(connected=True)

data = pd.read_csv('WordNet_list.csv', header=None)
occupation_relations_list = [(a, b) for a, b in data.values]

model = PoincareModel(occupation_relations_list, size=2, negative=8)
model.save('filename')
model = PoincareModel.load('filename')
model.train(epochs=5000)

relations_set = set(occupation_relations_list)
# 代表的な単語のみをラベルとして可視化する
major_occupation_list = ['性別','種別']
figure_title = ''
iplot(poincare_2d_visualization(model, relations_set, figure_title, num_nodes=None, show_node_labels=major_occupation_list))