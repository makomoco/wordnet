from gensim.models.poincare import PoincareModel
from gensim.viz.poincare import poincare_2d_visualization
from IPython import display
from plotly.offline import init_notebook_mode, iplot
import csv
import pandas as pd
import numpy as np

init_notebook_mode(connected=True)

# list_from_WordNet_1 学習用のリスト　タプルのリスト
# list_from_WordNet_2 フィルタ用のリスト　一次元リスト
# relations_set プロット用

# タプル形式で格納
data = pd.read_csv('WordNet_list.csv', header=None)
list_from_WordNet_1 = [(a, b) for a, b in data.values] 
# print(list_from_WordNet_1) #テスト→正常

# WordNet_list.csvを一次元配列（リスト）に格納
with open("WordNet_list.csv") as fp:
    csvList = list(csv.reader(fp))
list_from_WordNet_2 = [item for subList in csvList for item in subList]
# print(list_from_WordNet_2) #テスト→正常


# モデルの読み込み
model = PoincareModel.load('filename')

# 可視化ツールがset型しか受け付けないので整形
relations_set = set(list_from_WordNet_1)

# ラベルとして可視化する(mecabで抽出した名詞)
list_from_POL = [']

ls = [l for l in list_from_POL if l in list_from_WordNet_2] 

# WordNet内に登録されている単語のみ出力
# print('話題沸騰ポッド内の単語でWordNet内に登録されている単語のみ出力')
# print(ls) #テスト→正常

##########################
# プロット
# figure_title = ''
# iplot(poincare_2d_visualization(model, relations_set, figure_title, num_nodes=None, show_node_labels=ls))


# print(numpy.linalg.norm(a))
# print(numpy.linalg.norm(b))

###########################
# # ベクトル表示
# d = [] # リスト変換用
# e = [] # ls内の全単語に関して[x,y,'単語']の形でリスト化

# for l in ls:
#     c_1 = model.kv[l] # ベクトル化
#     d = c_1.tolist() # リストに変換
#     d.append(l) # [x,y,'単語']の形で保存
#     e.append(d)

# print('ベクトル結果表示')
# print(e)

distance_list = []
distance_and_word_list = []
distance_and_word_list_sorted = [] # distance_and_word_list_sorted[i][j] i:距離 j:単語

############################
# 距離計算
for l in ls:
    c_2 = model.kv[l]
    distance = np.linalg.norm(c_2) # ls内の全単語について原点からの距離を計算
    distance_list = [distance, l]
    distance_and_word_list.append(distance_list)


# print('距離表示')
# print(distance_and_word_list)

# print('ソートした結果を表示')
distance_and_word_list_sorted = sorted(distance_and_word_list)
# print(sorted(distance_and_word_list))

######################
# 指定した単語の距離を出力
# count_1 = 0 # カウント用
# ex_word = 'ソフトウェア'
# for i in distance_and_word_list_sorted:
#     if distance_and_word_list_sorted[count_1][1] == ex_word:
#         dis = distance_and_word_list_sorted[count_1][0] # ex_wordの距離出力
#         break
#     else:
#         count_1 += 1

#########################
# ある単語の全ての下位語を出力
# kaigo = []
# count_2 = 0
# for i in distance_and_word_list_sorted:
#     if distance_and_word_list_sorted[count_2][0] >= dis:
#         kaigo.append(distance_and_word_list_sorted[count_2][1])
#         count_2 += 1
#     else:
#         count_2 += 1

# print('「%s」より下位語を出力します' % ex_word)    
# print(kaigo)

#########################
# ある単語の全ての上位語を出力
# jouigo = []
# count_3 = 0
# for j in distance_and_word_list_sorted:
#     if distance_and_word_list_sorted[count_3][0] <= dis:
#         jouigo.append(distance_and_word_list_sorted[count_3][1])
#         count_3 += 1
#     else:
#         count_3 += 1

# print('「%s」より上位語を出力します' % ex_word)
# print(jouigo)

###########################
# 名詞がどれほど抽出できているか
# 正解のフーチャー図に記載されているクラス名
# correct_n =['給湯','給湯制御表示','給湯ボタン','給湯ロック/解除ボタン','状態表示','ロックランプ','給湯','ポンプ',
#             '温度制御','温度制御指示','保温設定ボタン','沸騰ボタン','温度制御方式','PID制御方式','温度制御テーブル方式','目標温度ON/OFF','沸騰','保温','高温モード','節約モード','ミルクモード','センサ','サーミスタ','蓋センサ',
#             '状態表示','保温ランプ','沸騰ランプ','温度表示','モード表示','加熱','ヒータ','ヒータ電源',
#             '水位検知','水位メータ','第N水位センサ','満水センサ',
#             'エラー検知','高温エラー','温度上がらずエラー','温度上がらずエラー',
#             'キッチンタイマ','タイマ起動','1分追加','タイマボタン','タイマ残り時間表示']

#####################################################
# フィーチャー図内の単語を形態素解析（ただのMecab）にかけたもの
correct_n = ['話題','沸騰','ポット','ver','給湯','給湯','制御','指示','給湯','ボタン','給湯','ロック','解除','ボタン','状態','表示','ロック','ランプ','給湯','ポンプ','温度','制御','温度','制御','指示','保温','設定','ボタン','沸騰','ボタン','温度','制御','方式','PID制御','方式','温度','制御','テーブル','方式','目標','温度','沸騰','保温','高温','モード','節約','モード','ミルク','モード','センサ','サーミスタ','蓋','センサ','状態','表示','保温','ランプ','沸騰','ランプ','温度','表示','モード','表示','加熱','ヒータ','ヒータ','電源','水位','検知','水位','メータ','N','水位','センサ','満水','センサ','エラー','検知','高温','エラー','温度','エラー','キッチン','タイマ','タイマ','起動','分','追加','タイマ','ボタン','タイマ','残り','時間','表示']
correct_n_set = set(correct_n) # 重複削除
correct_n_list = list(correct_n_set)

print('lsを出力(要素数は%d)' % len(ls))
print(ls)

print('フィーチャー図を出力(要素数は%d)' % len(correct_n_list))
print(correct_n_list)

###############################3
# 一致している要素を出力

# l1_l2_and = set(list_from_POL) & set(correct_n_list)
# l1_l2_and_list = list(l1_l2_and)
# print('POLとフィーチャー図で一致している名詞を出力')
# print(l1_l2_and_list)

l3_l2_and = set(ls) & set(correct_n_list)
l3_l2_and_list = list(l3_l2_and)
print('lsとフィーチャー図で一致している名詞を出力(要素数は%d)' % len(l3_l2_and_list))
print(l3_l2_and_list)

# l4_l2_and = set(list_from_WordNet_2) & set(correct_n_list)
# l4_l2_and_list = list(l4_l2_and)
# print('WordNet内の単語とフィーチャー図で一致している名詞を出力')
# print(l4_l2_and_list)