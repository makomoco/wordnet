from gensim.models.poincare import PoincareModel
from gensim.viz.poincare import poincare_2d_visualization
from IPython import display
from plotly.offline import init_notebook_mode, iplot
import csv
import pandas as pd
import numpy as np

import poincare03

init_notebook_mode(connected=True)

# 名詞がどれほど抽出できているか
# 正解のフーチャー図に記載されているクラス名
correct_n =['給湯','給湯制御表示','給湯ボタン','給湯ロック/解除ボタン','状態表示','ロックランプ','給湯','ポンプ',
            '温度制御','温度制御指示','保温設定ボタン','沸騰ボタン','温度制御方式','PID制御方式','温度制御テーブル方式','目標温度ON/OFF','沸騰','保温','高温モード','節約モード','ミルクモード','センサ','サーミスタ','蓋センサ',
            '状態表示','保温ランプ','沸騰ランプ','温度表示','モード表示','加熱','ヒータ','ヒータ電源',
            '水位検知','水位メータ','第N水位センサ','満水センサ',
            'エラー検知','高温エラー','温度上がらずエラー','温度上がらずエラー',
            'キッチンタイマ','タイマ起動','1分追加','タイマボタン','タイマ残り時間表示']

l1_l2_and = set(list_from_POL) & set(correct_n)
l1_l2_and_list = list(l1_l2_and)
print(l1_l2_and_list)