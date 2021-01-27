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
              [0.172545587317571, 0.7874105120849451]])

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


# コサイン類似度（正規化）
print(evaluate.cosine_similarity_normalized(evaluate.vector_normalized(x3), evaluate.vector_normalized(x10)))
