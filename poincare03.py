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

# ラベルとして可視化する
list_from_POL = ['話題沸騰ポットGOMA型要求仕様書', '版', '胡麻印', 'ほうびん株', 'ト ゙キュメント', 'ご利用', '著作物',
                         '著作権', '作成者', '所属', '組織', '゙所有', '著作権法', '保護', 'SESSAME', '著作者', '利用', '許諾',
                         '゙利用者個人', '使用許諾 ', '使用', '個人以外 ', '方', '゙', '場合', 'query sessame jp', '゙お問い合わせ', '゙さい',
                         '゙著作者', '権利著作物 ', '複製', '上演', '演奏', '公衆送信及', '゙送信可能化 ', '口述', '展示', '上映及', '゙頒布',
                         '貸与', '翻訳', '翻案', '二次的著作物', '目次', '機能要件', 'ハードウェア構成 ', '操作パネル部', '温度制御方式',
                         '温度制御仕様', 'エラー検知', 'システム', '動作', '制約事項', '今回設計', '沸騰ポット', 'ユーザに以下', '機能', '提供',
                         '家電製品', '゙す', '•ポット内', '水', '沸騰', '保温', '給湯', '•ユーザが指定', '時間', '゙きたら', 'ブザー', 'キッチンタイマ機能',
                         '以降', '章', 'ポット', '要求', '詳細', '説明', 'ハードウェア構成対象', '以下', 'よう', '外観', '蓋操作パネル', '給湯口', '取手',
                         '貯水部', '断熱性', 'ステンレス素材 ', 'ため', 'ポット内', '゙きるようになっています', '内部', '構成', 'ポンプ', '水路', '蓋センサ',
                         '満水センサ給水線', '水位センサ', 'サーミスタヒータ用電源', 'ヒータ', 'ここ', '用語', '意味', '次', 'とおり', '•満水センサ', '水位',
                         '許容上限', '゙うかを検出', 'セン', 'サ', '゙on', '時', '゙許容上限', 'こと', '•', 'n水位センサ', '検出', 'センサ', 'on', '位置', 'す',
                         '•蓋センサ', '蓋', '゙ている時', '•サーミスタ', '水温', '•ヒータ', '加熱', '•ヒータ用電源', '電力', '供給', '通常', '異常', '゙発生', 'off',
                         '遮断', '•給水線', 'ユーザ', '゙できる水量', '上限', '目印', '満水センサ', '若干下', '•ポンプ', '上', '゙て', '排出', '•水路', 'ポンプによって',
                         '゙られる水', '通路', '操作パネル部ポット上部', '操作パネル', 'ランプ', '温度モード表示窓', 'タイマ分', '沸騰保温水位', '温度', '高温節約ミルク',
                         '解除ロック', '保温設定', 'タイマ残り時間表示窓', '•タイマボタン', '水位メータ', 'ボタン', 'タイマ', '゙起動', '回', '毎', '追加', '•タイマ残り時間表示窓',
                         'タイムアップまでの残り時間分単位', '切り上', '゙表示', '•保温設定ボタン', '保温モード', '高温°C保温', '節約°C保温', 'ミルク°C保温モード', '設定', '高温',
                         '節約', 'ミルク', 'モードが', '•温度モード表示窓現在', '保温モード図中', '•解除ボタン給湯口', 'ロック解除', 'ロック中', '給湯ボタン', 'ロック', '解除',
                         '給湯中', '゙きません', '•ロックランプ給湯口', '゙ロック', '゙う', '点灯', '•給湯ボタン', '間中', '手', '停止', '•沸騰ボタン', 'カルキ抜き', '沸騰中', '中止', 
                         '保温状態', '•沸騰ランプ水', '゙終了', '消灯', '•保温ランプ沸騰中', '゙ない時', '沸騰ボタン押下等', '゙水', '•水位メータポット内', '表示', '関係', '対応', 
                         'インジケータセル', '複数', '呼', '゙れるランプにより構成', '数', '同数', 'セル', '゙on状態', '時水', '゙あると検出', '゙点灯', '例', '間', 'on off', '制御', '制御方式',
                         '制御周期', '操作量', '下図', '゙操作量', '゙けヒータ', '上記', '決定', '方式', '゙あります', 'PID制御方式', '温度特性', '比例係数Kp', '微分係数Kd', '積分係数Ki',
                         '式', '゙時間 t', '操作量 M', '゙計算', '目標温度 Tg', '⊿T', 'E', 'T T', 'T', 't', 'M E Kp E Ki ∫Edt Kd dE dt 水温°C', '数式', '展開', '前回', '今回', '差 ⊿M',
                         '⊿M M M Kp T T Ki Tg T Kd T T T', 'の', 'M M ⊿M', '゙し', '≦M ≦', '温度制御テーブル方式', '図', 'あらかじめ', 'テーブル', '保存', '操作量決定時', '参照', 'E °C',
                         '≧≦', '⊿T °C ≧', '≦', '目標温度ONOFF方式', '温度上昇中', '目標温度', '温度下降中', 'ヒータon時', 'ヒータoff時', '水温°C', 'offon', '境', 'ヒステリシス', '方法',
                         '温度 T', 'off on off on', '仕様', '゙られた場合温度制御可能', '゙沸騰状態', '移行', '゙°C', '後', '分間加熱', 'その後保温状態', '温度制御', '操作量算出', '目標温度ONOFF方式ヒステリシス', '適用', '分', '沸騰状態', '場合高温モードが設定', '°C', '場合節約モードが設定', '場合ミルクモードが設定', '沸騰ボタン押下', '強制沸騰', '制御仕様', '同様', '保温設定ボタン', '変更', '場合移行', '仕様毎', '操作量算出方法', '機種', '゙故障誤動作', 'エラー', '検知', 'これ', '異常過熱', '火災等', '危険', '回避',
                         'サーミスタ', '故障', 'ソフトウェア', '゙はエラー', '゙きないため', 'ハードウェア的 ', '断線', '安全', '確保',
                         '及', '゙ポンプ', '故障誤動作', '設計', 'もの', '種類', '分類', '゙できます', '高温エラー', '゙停止', '゙きなくなった場合', '発生', 'ヒータ用電源', '秒間ブザー', '高温エラー検知', 
                         '温度上', '゙らずエラーこれ', '゙動作', '゙不安定', 'ヒータ制御中', '一定周期', '゙水温', '゙°C下', '゙り', '前回検出', '今回検出', '水温検出周期', '最初', '°C水温', '゙すが', 
                         '今回検出温度前回検出温度', '゙エラー', '番目', '゙温度上', '゙らずエラー', '水温°C目標温度', '今回検出温度', '前回検出温度', 'b温度上', '゙ない例', '今回検出温度エラー検知', 
                         'c温度上', '゙検知', 'システム全体', '動作仕様', '゙なりません', '゙off', '゙可能', 'それ以外', '沸騰ボタン', '•蓋', 'とき', '沸騰ランプ及', '゙保温ランプは消灯', '•保温モード', '際', 
                         '゙なかった場合', '必', '゙一度沸騰', '自然', 'ながら設定温度', '•タイマ', '最大時間', '゙設定', '゙きます', '•ユーザ', 'ボタンタイマ', '制約時', '•ユーザが設定', 'タイムアウト時', 
                         '゙沸騰状態終了時', '•T B D', 'ハードウェア', '要件', '゙確定', '゙T B D', '要求仕様書', '教育用資料', '環境', '適宜', '制約', '゙いて結構', '発行履歴', 
                         '話題沸騰ポットGOMA型要求仕様書年月日初版発行', '年月日', '版発行']

ls = [l for l in list_from_POL if l in list_from_WordNet_2] 

# WordNet内に登録されている単語のみ出力
# print('話題沸騰ポッド内の単語でWordNet内に登録されている単語のみ出力')
# print(ls) #テスト→正常

# プロット
# figure_title = ''
# iplot(poincare_2d_visualization(model, relations_set, figure_title, num_nodes=None, show_node_labels=ls))


# print(numpy.linalg.norm(a))
# print(numpy.linalg.norm(b))


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


# ある単語の全ての下位語を表示
count_1 = 0 # カウント用
ex_word = '安全'
for i in distance_and_word_list_sorted:
    if distance_and_word_list_sorted[count_1][1] == ex_word:
        dis = distance_and_word_list_sorted[count_1][0] # ex_wordの距離出力
        break
    else:
        count += 1

kaigo = []
count_2 = 0
for i in distance_list:
    if distance_and_word_list_sorted[count_2][0] >= dis:
        kaigo.append(distance_and_word_list_sorted[count_2][1])
        count_2 += 1
    else:
        count_2 += 1

print('%sより下位語を出力します' % ex_word)    
print(kaigo)


