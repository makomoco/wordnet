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

# モデルの読み込み(５次元)
model = PoincareModel.load('filename_5')

# 可視化ツールがset型しか受け付けないので整形
relations_set = set(list_from_WordNet_1)

list_from_POL = ['単位', '時間', '要求', 'n', '秒', '一', 'dE', 'ため', '下', '事項', 'Kp', '方法', '火災',
                 '結構', '目次', 'セル', '係数', '通路', '保温', '残り', '問い合わせ', '許容', '水路', '抜き', 
                 '確保', '次', '取手', 'Ki', 'ドキュメント', '同様', 'ソフトウェア', 'インジケータ', '発生', '積分', 
                 '目', 'モード', 'Kd', '境', 'D', 'sessame', '窓', '後', '番', 'す', '用', '各', 'PID制御', 
                 '検知', '通常', '等', '上映', '水', '線', '押下', '水温', '化', 'サ', '高温', '安全', 'T', 
                 '上演', 'jp', '関係', '確定', 'ヒータ', '方', 'びん', 'ランプ', 't', '給水', '間中', '量', 
                 '権利', 'ユーザ', 'テーブル', 'ここ', '停止', '現在', '構成', '目印', '同数', 'Tg', 'b', 
                 '沸騰', '全体', 'B', '機能', '起動', '回', '決定', '下降', '保存', '差', '算出', 'query', 
                 '間', 'ポット', '適宜', '翻訳', '著作権', '上部', '履歴', '参照', '型', '著作者', '家電製品', 
                 '検出', '的', '計算', '章', '比例', '展示', '年月日', 'GOMA', '上限', 'まほう', 'とき', '初版', 
                 '電源', '水位', '書', '保護', 'c', '給湯', '供給', 'C', 'これ', '分類', '話題', '頒布', 'ブザー', 
                 '使用', '部', '蓋', 'on', '時', '排出', '解除', '終了', '数', '方式', 'off', '対応', '微分係数', 
                 '異常', '数式', '分間', '翻案', '移行', '意味', '要求仕様', '不安定', '節約', 'ハードウェア', '内部', 
                 '利用', '一定', 'SESSAME', '口', 'その後', 'ご', '教育', '自然', 'とおり', '者', '加熱', '可能', 
                 '種類', '環境', '式', '最初', '株', '資料', '誤動作', '上昇', 'ロック', '所属', '制御', '指定', '物', 
                 'ボタン', '以下', '機種', '故障', '前回', '発行', '説明', '水量', '手', '適用', 'Edt', '貯水', '用語', 
                 '特性', '胡麻', '操作', '演奏', '状態', '複製', '下図', '許諾', '設計', 'E', '度', '展開', '若干', 
                 'メータ', '複数', '個人', '対象', '断線', '追加', '例', '著作物', 'dt', '制約', '口述', 'セン', '点灯', 
                 '消灯', '著作', 'ステンレス', '毎', '位置', '場合', '二次的著作物', '提供', 'エラー', '内', 'サーミスタ', 
                 'パネル', '外観', '中止', '要件', 'ヒステリシス', '断熱', '周期', '作成者', '送信', '上記', '回避', '以外', 
                 '過熱', 'もの', '所有', 'カルキ', '公衆', '危険', '本', '組織', '以降', '性', 'ミルク', '図', '最大', 
                 'タイムアップ', '動作', 'システム', '満水', '設定', 'ポンプ', '貸与', '表示', '詳細', '版', '際', 'タイマ', 
                 'こと', '切り上げ', '目標', '電力', '今回', '素材', '印', 'お', '中', '仕様書', '温度', '分', 'M', 
                 '利用者', '遮断', 'センサ', '強制', '仕様', '変更', 'それ', 'よう', '法', 'キッチン']



ls = [l for l in list_from_POL if l in list_from_WordNet_2] 

###########################
# フィーチャー図内の単語を形態素解析（ただのMecab）にかけたもの
correct_n = ['話題','沸騰','ポット','ver','給湯','給湯','制御','指示','給湯','ボタン','給湯','ロック','解除','ボタン','状態','表示','ロック','ランプ','給湯','ポンプ','温度','制御','温度','制御','指示','保温','設定','ボタン','沸騰','ボタン','温度','制御','方式','PID制御','方式','温度','制御','テーブル','方式','目標','温度','沸騰','保温','高温','モード','節約','モード','ミルク','モード','センサ','サーミスタ','蓋','センサ','状態','表示','保温','ランプ','沸騰','ランプ','温度','表示','モード','表示','加熱','ヒータ','ヒータ','電源','水位','検知','水位','メータ','N','水位','センサ','満水','センサ','エラー','検知','高温','エラー','温度','エラー','キッチン','タイマ','タイマ','起動','分','追加','タイマ','ボタン','タイマ','残り','時間','表示']
correct_n_set = set(correct_n) # 重複削除
correct_n_list = list(correct_n_set)

###########################
l3_l2_and = set(ls) & set(correct_n_list)
l3_l2_and_list = list(l3_l2_and)
# print('lsとフィーチャー図で一致している名詞を出力(要素数は%d)' % len(l3_l2_and_list))
# print(l3_l2_and_list)

###########################
#５次元ベクトル表示
# d = [] # リスト変換用
# e = [] # 内の全単語に関して[x1,x2,x3,x4,x5,'単語']の形でリスト化

# for l in l3_l2_and_list:
#     c_1 = model.kv[l] # ベクトル化
#     d = c_1.tolist() # リストに変換
#     d.append(l) # [x1,x2,x3,x4,x5,'単語']の形で保存
#     e.append(d)

# print('ベクトル結果表示')
# print(e)

############################
# 複合語の５次元平均ベクトルを求める
# aa_1 = model.kv['加熱']
# aa_2 = model.kv['制御']
# aa_3 = model.kv['テーブル']
# aa_4 = model.kv['方式']

# bb_1 = aa_1.tolist()
# bb_2 = aa_2.tolist()
# bb_3 = aa_3.tolist()
# bb_4 = aa_4.tolist()

# avg_x1 = (bb_1[0]) / 1
# avg_x2 = (bb_1[1]) / 1
# avg_x3 = (bb_1[2]) / 1
# avg_x4 = (bb_1[3]) / 1
# avg_x5 = (bb_1[4]) / 1

# avg = [avg_x1,avg_x2,avg_x3,avg_x4,avg_x5]

# print('平均ベクトルを算出')
# print(avg)

# # np配列化
# avg_np = np.array(avg)
# print(avg_np)
# # 距離計算
# distance = np.linalg.norm(avg_np) # l3_l2_and_list内の全単語について原点からの距離を計算（ユークリッド距離）
#                                     # ユークリッド距離で計算して良い（https://ja.wikipedia.org/wiki/ポワンカレの円板モデル　参照）
# d_p = 1 + 2 * ((distance**2) / (1 - (distance**2))) #arccoshの中身
# distance_p = np.arccosh(d_p) 
# print('距離を出力')
# print(distance_p)

# 複合語新処理(v(w1,w2)=w1/|w1| + w2/|w2|)
aa_1 = model.kv['ロック']
aa_2 = model.kv['ランプ']
# aa_3 = model.kv['テーブル']
# aa_4 = model.kv['方式']

bb_1 = aa_1.tolist()
bb_2 = aa_2.tolist()

cc_1 = [bb_1[0] / np.linalg.norm(aa_1), bb_1[1] / np.linalg.norm(aa_1), bb_1[2] / np.linalg.norm(aa_1), bb_1[3] / np.linalg.norm(aa_1), bb_1[4] / np.linalg.norm(aa_1)]
cc_2 = [bb_2[0] / np.linalg.norm(aa_2), bb_2[1] / np.linalg.norm(aa_2), bb_2[2] / np.linalg.norm(aa_2), bb_2[3] / np.linalg.norm(aa_2), bb_2[4] / np.linalg.norm(aa_2)]

w_w1_w2 = [cc_1[0]+cc_2[0],cc_1[1]+cc_2[1],cc_1[2]+cc_2[2],cc_1[3]+cc_2[3],cc_1[4]+cc_2[4]]

print('複合語ベクトルを出力')
print(w_w1_w2)

# np配列化
avg_np = np.array(w_w1_w2)
# print(avg_np)
# 距離計算
distance = np.linalg.norm(avg_np) # l3_l2_and_list内の全単語について原点からの距離を計算（ユークリッド距離）
                                     # ユークリッド距離で計算して良い（https://ja.wikipedia.org/wiki/ポワンカレの円板モデル　参照）

# ノルムが１以上の際は、ベクトル/ノルムを行う
if distance >= 1:
    w_w1_w2_2 = w_w1_w2 / distance
    print(w_w1_w2_2.tolist())
    avg_np_2 = np.array(w_w1_w2_2.tolist())
    print(avg_np_2)
    distance_2 = np.linalg.norm(avg_np_2)
    print('distance_2 =')
    print(distance_2)
else:
    print('distance =')
    print(distance)

# if distance_2 >= 1:
#     w_w1_w2_3 = w_w1_w2_2 / distance_2
#     print(w_w1_w2_3.tolist())
#     avg_np_3 = np.array(w_w1_w2_3.tolist())
#     print(avg_np_3)
#     distance_3 = np.linalg.norm(avg_np_3)
#     print('distance_3 =')
#     print(distance_3)  
# else:
#     print('distance_2 =')
#     print(distance_2)   

d_p = 1 + 2 * ((distance_2**2) / (1 - (distance_2**2))) #arccoshの中身
print(d_p)
distance_p = np.arccosh(d_p) 
print('距離を出力')
print(distance_p)
