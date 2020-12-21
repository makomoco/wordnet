from gensim.models.poincare import PoincareModel
from gensim.viz.poincare import poincare_2d_visualization
from IPython import display
from plotly.offline import init_notebook_mode, iplot
import pandas as pd

col_names = ['c{0:02d}'.format(i) for i in range(10)]
occupation_relations_list = [(a, b) for a, b in pd.read_csv('occupation_relations.csv', header=None, encoding="shift-jis", names=col_names).as_matrix()]

model = PoincareModel(occupation_relations_list, size=2, negative=7)
model.train(epochs=500)

relations_set = set(occupation_relations_list)
# 代表的な職種のみをラベルとして可視化する
#major_occupation_list = ['Engineer', 'Designer', 'Web', '取締役', 'Freelance', 'Intern', 'Programmer', 'Founder', 'Director', 'Marketer', 'Software Engineer']
major_occupation_list = ['Designer', 'Engineer']
figure_title = ''
iplot(poincare_2d_visualization(model, relations_set, figure_title, num_nodes=None, show_node_labels=major_occupation_list))