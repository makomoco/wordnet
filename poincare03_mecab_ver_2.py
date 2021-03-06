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

# ラベルとして可視化する(mecabで重複を削除しつつ抽出した名詞句)
# list_from_POL = ['家電製品', '作成者', '間中', 'M', '番', 'モード', 'n', '翻訳', '検出', 'エラー',
#                  '周期', '解除', '下図', '可能', '危険', '参照', '水', '下降', '的', 'ステンレス',
#                  '切り上げ', '内部', 'off', '印', 'E', 'dE', '安全', '種類', '表示', '算出', 'ため',
#                  '分類', '教育', '秒', '型', 'パネル', '節約', '検知', '仕様', '説明', '口述', '貸与',
#                  'ブザー', 'これ', '用', '高温', '決定', '差', '素材', '要求', 'Edt', '境', '適用',
#                  'ロック', '分間', '複製', '上映', 'サ', '上記', 'びん', '比例', '同様', '目', '間',
#                  '移行', '機種', 'b', '各', '制御', '下', '手', '目標', 'ソフトウェア', '上限', '設計', 
#                  '回', '供給', '発生', '水路', '故障', '満水', 'キッチン', '式', 'query', 'す', '提供', 'テーブル', 
#                  '以降', '誤動作', '単位', '通路', '複数', '本', '著作権', '中止', '終了', 'インジケータ', '保護', 
#                  '回避', 'それ', 'on', '話題', 'B', '株', '消灯', '構成', '若干', '性', '上昇', '蓋', '図', '状態', 
#                  '目次', '部', '一', 'ヒータ', 'ボタン', '内', '位置', '機能', 'T', '問い合わせ', '停止', '制約', 
#                  'PID制御', '演奏', 'お', '胡麻', 'ポンプ', '使用', '個人', '通常', '沸騰', '事項', 'ランプ', '火災', 
#                  'jp', 'ご', 'dt', '保存', 'c', '著作物', 'D', '量', 'ここ', 'ハードウェア', 'ドキュメント', '化', 
#                  '許諾', '起動', '権利', 'よう', '過熱', '結構', '者', '全体', '貯水', '発行', '対応', '組織', 'メータ', 
#                  '設定', 'まほう', 'タイムアップ', '強制', '電力', '以下', '章', '異常', '線', '数', '給湯', '変更', 
#                  '方', '時', '初版', '二次的著作物', '一定', '数式', 'とおり', '自然', 'ユーザ', '送信', 'セン', '後', 
#                  't', '口', '方法', '資料', '物', '保温', '水位', 'セル', '環境', '適宜', '特性', 'SESSAME', '温度', 
#                  '例', '不安定', '微分係数', '方式', '時間', 'サーミスタ', '用語', '上部', '利用', '係数', '前回', 
#                  '指定', '上演', '意味', '確保', 'Kp', '操作', 'こと', '次', '加熱', '残り', '最初', '関係', '同数', 
#                  '中', '動作', '今回', '水量', '等', '計算', 'その後', '追加', '許容', '要求仕様', 'Ki', 'Tg', 
#                  'ヒステリシス', '書', '最大', '仕様書', '度', '展示', 'センサ', '断線', '点灯', 'もの', '対象', 
#                  '履歴', '翻案', 'ミルク', '以外', '年月日', '版', '断熱', 'カルキ', '押下', '所属', '電源', '毎', 
#                  '抜き', '著作', 'Kd', '水温', '確定', '頒布', '場合', '法', '著作者', '給水', 'sessame', 'とき', 
#                  '遮断', '取手', 'ポット', '分', '目印', 'C', '排出', 'GOMA', '現在', '要件', 'タイマ', '公衆', 
#                  'システム', '所有', '窓', '展開', '利用者', '詳細', '際', '外観', '積分']

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

list_form_POL_2 = ['水量', '使用', '指定', 'こと', '水温', 'C', '量', '部', '場合', 'ミルク', 'b', '株', 'Kp', 'ため', 'ハードウェア', '方', '追加', '回', '後', '異常', '微分係数', 'query', 'テーブル', 'D', 'カルキ', 'ご', '問い合わせ', 'T', '特性', '通常', '度', '積分', '章', 'サ', '用', '押下', '家電製品', '二次的著作物', 'ヒステリシス', '沸騰', 'ドキュメント', '組織', '回避', '誤動作', '適宜', '分類', 'エラー', 'ステンレス', '給湯', 'サーミスタ', 'とおり', '遮断', '環境', '若干', '算出', '自然', '著作', '複製', '確定', 'ブザー', '演奏', '展示', '要求', '最初', '残り', '方式', '保温', '停止', 'インジケータ', '時間', '係数', '所属', '強制', 'ランプ', '日', '貯水', '加熱', '検知', 'ロック', 'まほう', '法', '構成', '利用者', 'ソフトウェア', 'お', '内', '前回', '機種', '抜き', '的', 'c', '現在', '参照', '線', '目印', 'メータ', 'SESSAME', '上記', '方法', '機能', '間中', '全体', '保護', 'off', '月', '目', '外観', 'システム', '者', '計算', '一定', '危険', '化', 'モード', '貸与', '教育', '著作物', '対応', '展開', '書', '式', '数', 'これ', '目次', '安全', '例', 'Tg', '給水', '電源', '設定', '物', '性', '今回', '通路', 'on', '消灯', '秒', 'B', '中止', '状態', '動作', '要件', 'ヒータ', '等', '翻案', '所有', '詳細', 'PID制御', '履歴', '公衆', '許容', '比例', '供給', '終了', '毎', '上部', '説明', '型', '事項', '決定', 'よう', '位置', '作成者', '蓋', 'sessame', '断線', '翻訳', 'E', '胡麻', '番', '制御', '同様', '用語', '上限', '制約', '仕様', 'す', '発生', '適用', '種類', 'とき', '結構', '水路', '上映', '設計', '下降', '中', '起動', '上昇', '個人', '過熱', '各', 'dt', '水位', '素材', '分', 'タイムアップ', '発行', '口述', '検出', '本', '以下', 'ここ', 'Kd', '要求仕様', '下', '切り上げ', '差', '満水', '分間', '火災', '数式', 'タイマ', '対象', 'その後', '著作者', '移行', '点灯', '初版', '解除', 'セン', '故障', '可能', '手', '際', '頒布', '温度', 'キッチン', '同数', '目標', '保存', '高温', '窓', '内部', 't', '下図', 'ボタン', '許諾', '仕様書', 'jp', '操作', '以外', 'M', '送信', '資料', '間', 'センサ', '時', '不安定', 'dE', '著作権', 'Ki', '以降', '変更', '版', 'もの', '複数', 'びん', '印', '一', 'ポット', '利用', '上演', 'ユーザ', '口', '取手', '断熱', 'n', '表示', '図', '関係', '境', '最大', '話題', '確保', '年', 'GOMA', 'それ', 'ポンプ', '権利', '電力', '節約', '単位', '次', '意味', 'パネル', 'セル', '排出', '水', '提供', '周期']

print(len(list_from_POL))
print(len(list_form_POL_2))


unl = set(list_from_POL) & set(list_form_POL_2)
unl_list = list(unl)
print('POLとPOL_2で一致している名詞を出力')
print(unl_list)
print(len(unl_list))

result_111 = list(set(list_from_POL) - unl)
print('POLとの差分')
print(result_111)
result_222 = list(set(list_form_POL_2) - unl)
print('POL2との差分')
print(result_222)

# 結果
# POLとの差分
# ['Edt', '年月日']
# POL2との差分
# ['年', '日', '月']　→　特に影響なし？


ls = [l for l in list_from_POL if l in list_from_WordNet_2] 

##########################################
# 複合語の平均ベクトルを求める
# aa_1 = model.kv['加熱']
# # aa_2 = model.kv['制御']
# # aa_3 = model.kv['テーブル']
# # aa_4 = model.kv['方式']

# bb_1 = aa_1.tolist()
# # bb_2 = aa_2.tolist()
# # bb_3 = aa_3.tolist()
# # bb_4 = aa_4.tolist()

# avg_x = (bb_1[0] + bb_2[0] + bb_3[0] + bb_4[0]) / 4
# avg_y = (bb_1[1] + bb_2[1] + bb_3[1] + bb_4[1]) / 4

# avg = [avg_x,avg_y]

# print('平均ベクトルを算出')
# print(avg)

# # np配列化
# avg_np = np.array(avg)
# print(avg_np)
# 距離計算
# distance = np.linalg.norm(avd_np) # l3_l2_and_list内の全単語について原点からの距離を計算（ユークリッド距離）
#                                     # ユークリッド距離で計算して良い（https://ja.wikipedia.org/wiki/ポワンカレの円板モデル　参照）
# d_p = 1 + 2 * ((distance**2) / (1 - (distance**2))) #arccoshの中身
# distance_p = np.arccosh(d_p) 
# print('距離を出力')
# print(distance_p)


# WordNet内に登録されている単語のみ出力
# print('話題沸騰ポッド内の単語でWordNet内に登録されている単語のみ出力')
# print(ls) #テスト→正常

##########################
# プロット
# figure_title = ''
# iplot(poincare_2d_visualization(model, relations_set, figure_title, num_nodes=None, show_node_labels=ls))

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

# print('lsを出力(要素数は%d)' % len(ls))
# print(ls)

# print('フィーチャー図を出力(要素数は%d)' % len(correct_n_list))
# print(correct_n_list)

###############################3
# 一致している要素を出力

# l1_l2_and = set(list_from_POL) & set(correct_n_list)
# l1_l2_and_list = list(l1_l2_and)
# print('POLとフィーチャー図で一致している名詞を出力')
# print(l1_l2_and_list)

l3_l2_and = set(ls) & set(correct_n_list)
l3_l2_and_list = list(l3_l2_and)
# print('lsとフィーチャー図で一致している名詞を出力(要素数は%d)' % len(l3_l2_and_list))
# print(l3_l2_and_list)

# l4_l2_and = set(list_from_WordNet_2) & set(correct_n_list)
# l4_l2_and_list = list(l4_l2_and)
# print('WordNet内の単語とフィーチャー図で一致している名詞を出力')
# print(l4_l2_and_list)


# print(numpy.linalg.norm(a))
# print(numpy.linalg.norm(b))

###########################
# # ベクトル表示
# d = [] # リスト変換用
# e = [] # ls内の全単語に関して[x,y,'単語']の形でリスト化

# for l in l3_l2_and_list:
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
# for l in l3_l2_and_list:
#     c_2 = model.kv[l]
#     distance = np.linalg.norm(c_2) # l3_l2_and_list内の全単語について原点からの距離を計算（ユークリッド距離）
#                                     # ユークリッド距離で計算して良い（https://ja.wikipedia.org/wiki/ポワンカレの円板モデル　参照）
#     d_p = 1 + 2 * ((distance**2) / (1 - (distance**2))) #arccoshの中身
#     distance_p = np.arccosh(d_p) # ポアンカレ距離
#     distance_list = [distance_p, l]
#     distance_and_word_list.append(distance_list)

distance_and_word_list_hukugougo = [[0.7861080035099905,'状態表示'],
                                    [3.4193208611866024,'ロックランプ'],
                                    [10.158806403323792,'ポンプ'],
                                    [0.26675220818771983,'温度制御'],
                                    [10.475748046199035,'沸騰ボタン'],
                                    [0.8754122811226502,'温度制御方式'],
                                    [1.2445454596465897,'温度制御テーブル方式'],
                                    [11.424656451583653,'沸騰'],
                                    [2.27821317806947,'高温モード'],
                                    [0.16843167788701552,'節約モード'],
                                    [0.07997333800440233,'ミルクモード'],
                                    [10.57936080429842,'センサ'],
                                    [0.43173430373722466,'蓋センサ'],
                                    [2.452639002585924,'沸騰ランプ'],
                                    [1.2457106114917664,'温度表示'],
                                    [1.4750406678625425,'モード表示'],
                                    [10.52386588053033,'加熱'],
                                    [1.151991689681557,'水位検知'],
                                    [0.009690482362774486,'水位メータ'],
                                    [0.6534839647192356,'水位センサ'],
                                    [1.3134649070610038,'エラー検知'],
                                    [1.3369774421893466,'高温エラー'],
                                    [2.231547416467637,'分追加']]

# print('距離表示')
# print(distance_and_word_list)

# print('ソートした結果を表示')
# distance_and_word_list_sorted = sorted(distance_and_word_list_hukugougo)
# print(sorted(distance_and_word_list_hukugougo))

# print("WordNetに登録されている単語かどうか")
# print('タイマ' in list_from_WordNet_2)
# print('フィルタをかけたあとのリストに入っているかどうか')
# print('タイマ' in ls)
# print('フィーチャー図とフィルタ後のリストどちらにも存在するかどうか')
# print('タイマ' in l3_l2_and_list)

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






