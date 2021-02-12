import numpy as np
import evaluate

X = np.array([[0.3700392572517431, -0.054217320035697576],
              [0.9285453094598232, 0.1226138645608977],
              [0.8461846202443636, -0.5327444664870183],
              [-0.07025265430212957, 0.11244948549446376],
              [0.6053371100684337, 0.7958983225501188],
              [-0.3432702926325633, 0.227368367032959],
              [-0.4971757334908846, 0.24145998279690128],
              [0.6099846774291194, 0.7923856403161927],
              [-0.663181791608394, -0.4721969376981317],
              [-0.011595044009778233, 0.08321335755076607],
              [-0.0015602001755750106, 0.03993490482845233],
              [0.9824927377900302, -0.18602764033020155],
              [0.0057430216464057215, -0.21249786401585535],
              [0.7921946008405585, 0.2838382909687912],
              [-0.24856050292989046, -0.4941169784452461],
              [-0.6179601048889836, -0.10983231769525718],
              [-0.7656181448807534, -0.6432117177268286],
              [-0.5099075780467606, -0.10066441607718274],
              [0.003562934646982263, 0.0032835181415117876],
              [0.1535634311827116, 0.2757090723133874],
              [0.3276522337492922, -0.47395453090322276],
              [0.33668437655249356, -0.47716032815206383],
              [0.172545587317571, 0.7874105120849451],          
              [0.5527920584021144, 0.21646590093855989], # x23
              [-0.8222812647862052, -0.5690141785895462],
              [0.9976739348912855, -0.06747619262506549],
              [-0.21010588306001188, -0.965190759713077],
              [-0.48779436735312176, -0.8609013489638148],
              [0.11928334601825391, -0.06634442368499421],
              [-0.3026122000452023, 0.030383192981625874]])

x0 = X[0] # 状態表示
x1 = X[1] # ロックランプ
x2 = X[2] # ポンプ
x3 = X[3] # 温度制御
x4 = X[4] # 沸騰ボタン
x5 = X[5] # 温度制御方式
x6 = X[6] # 温度制御テーブル方式
x7 = X[7] # 沸騰
x8 = X[8] # 高温モード
x9 = X[9] # 節約モード
x10 = X[10] # ミルクモード
x11 = X[11] # センサ
x12 = X[12] # 蓋センサ
x13 = X[13] # 沸騰ランプ
x14 = X[14] # 温度表示
x15 = X[15] # モード表示
x16 = X[16] # 加熱
x17 = X[17] # 水位検知
x18 = X[18] # 水位メータ
x19 = X[19] # 水位センサ
x20 = X[20] # エラー検知
x21 = X[21] # 高温エラー
x22 = X[22] # 分追加

x23 = X[23] # 話題沸騰ポッド
x24 = X[24] # サーミスタ
x25 = X[25] # ヒータ
x26 = X[26] # キッチンタイマ
x27 = X[27] # タイマ起動
x28 = X[28] # タイマボタン
x29 = X[29] # タイマ残り時間表示


# コサイン類似度（正規化）
# print(evaluate.cosine_similarity_normalized(evaluate.vector_normalized(x26), evaluate.vector_normalized(x29)))

# コサイン類似度結果(上位語,下位語)
cos_sim_l = [[0.9619423890352065,('状態表示','ロックランプ')],
             [0.35428148826605155,('温度制御','沸騰ボタン')],
             [0.9100618774256413,('温度制御','温度制御方式')],
             [0.3488275405843201,('温度制御','沸騰')],
             [-0.0602907737663847,('温度制御','高温モード')],
             [0.9131016628975764,('温度制御','節約モード')],
             [0.8681321606916226,('温度制御','ミルクモード')],
             [-0.6783729005750887,('温度制御','センサ')],
             [-0.6471964909972727,('温度制御','状態表示')],
             [-0.13985220642049412,('温度制御','加熱')],
             [0.9911814841039721,('温度制御方式','温度制御テーブル方式')],
             [0.21251395707575876,('センサ','蓋センサ')],
             [0.882555471877814,('状態表示','沸騰ランプ')],
             [-0.31513024415239543,('状態表示','温度表示')],
             [-0.9488005806720523,('状態表示','モード表示')],
             [-0.8526821917637258,('水位検知','水位メータ')],
             [-0.6465811801880053,('水位検知','水位センサ')],
             [0.9999539132401888,('エラー検知','高温エラー')],

            [0.8684569675045664,('話題沸騰ポッド','状態表示')],
            [0.5937207414822914,('話題沸騰ポッド','ポンプ')],
            [-0.184129465446841,('話題沸騰ポッド','温度制御')],
            [-0.9841427700604741,('話題沸騰ポッド','水位検知')],
            [0.22957541843413137,('話題沸騰ポッド','エラー検知')],
            [-0.5543417225009764,('話題沸騰ポッド','キッチンタイマ')],
            [-0.7020955359832202,('センサ','サーミスタ')],
            [-0.72050828179146,('加熱','ヒータ')],
            [0.9549913159713612,('キッチンタイマ','タイマ起動')],
            [-0.9999990460765702,('キッチンタイマ','分追加')],
            [0.2890603409279182,('キッチンタイマ','タイマボタン')],
            [0.11402321482111775,('キッチンタイマ','タイマ残り時間表示')]]

print(sorted(cos_sim_l, reverse=True))

i = 0
cos_sim_para = []
for l in cos_sim_l:
    if cos_sim_l[i][0] >= 0.8:
        cos_sim_para.append(l)
        i = i + 1
    else:
        i = i + 1


print(cos_sim_para)
        