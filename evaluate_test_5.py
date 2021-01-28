import numpy as np
import evaluate

X = np.array([[-0.13949060558276688, 0.005020203926432515, -0.3499690358569048, -0.23125462170925631, 0.2418104027131034],
              [-0.4875602189575885, -0.2999970335234154, -0.3631689575944946, -0.3744150644586629, 0.01496341254089456],
              [0.23374270182832188, -0.607841438072171, 0.10009372501026872, -0.37104287162185956, -0.6520473306169605],
              [0.040516277782331175, -0.5579579940692903, -0.4931158033999185, -0.11104532329488094, -0.2726315300750329],
              [-0.1293797895165669, -0.04359087150475405, -0.23215796554429846, 0.409498456958563, -0.04432845731332581],
              [0.026840377247649327, -0.2508675980662786, -0.5709462759173055, -0.2655706319694367, -0.1502438064292733],
              [-0.05950912238330804, -0.3045590191899811, -0.45074455461463503, -0.34477758551452853, -0.2570425386139621],
              [-0.6874057989094654, 0.5557062728742252, -0.18520102100271635, 0.35581831666420544, 0.23922581414808905],
              [-0.14097505757770928, 0.2227544198030097, -0.4939753086628602, -0.22644476897430565, -0.0052445336922561266],
              [-0.0694157946248189, 0.32488030646164895, 0.02821284556997606, 0.2621316603878773, -0.23130885187789],
              [-0.0816694758530619, -0.014984003951612423, 0.08883715483573645, -0.18328120690962368, -0.19789417541358081],
              [0.36359544007736166, -0.2893608261312537, -0.15880880375714296, -0.7807507727925727, -0.3835702198405224],
              [-0.03546796964414217, 0.07042888706289302, 0.11406353356561152, -0.668273745674315, -0.3956993955273216],
              [-0.49485429813499426, 0.010346511418042714, -0.1791171440753557, -0.1374259233599718, -0.10041811406091432],
              [-0.10840818697030026, 0.041525043490432734, -0.4946964391155088, -0.23075404162683194, 0.34790444782122726],
              [-0.3071195229549284, 0.5720137821171304, -0.16234732776006575, -0.18709770796139083, 0.39155335585869455],
              [0.219578420023898, 0.1930191244146536, 0.15782461619713045, 0.9110147951286794, 0.23967530862189415],
              [-0.1494910392206757, -0.11057384664425561, -0.4195477242806652, -0.15427831603664305, 0.04688697109081252],
              [-0.05959712939360129, -0.3506757181640591, 0.4222754955215101, -0.5597877517969434, 0.005679619904453752],
              [0.0310918734423046, -0.3595823812880985, -0.10289761952619737, -0.8102273481506251, -0.25090444313031673],
              [-0.2708886640627425, 0.30858366420637584, -0.5673153113654523, 0.5761979850148715, 0.07031219311327393],
              [-0.24086765734544607, 0.03705653393762795, -0.6166695939671913, 0.1649311359828877, -0.06224766113620252],
              [0.17295219559663388, -0.434740279801346, -0.3359330329390141, -0.19903886211421384, 0.09480547318059485]
])

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
print(evaluate.cosine_similarity_normalized(evaluate.vector_normalized(x0), evaluate.vector_normalized(x1)))

# コサイン類似度結果(上位語,下位語)
# cos_sim_l = [[,('状態表示','ロックランプ')],
#              [,('温度制御','沸騰ボタン')],
#              [,('温度制御','温度制御方式')],
#              [,('温度制御','沸騰')],
#              [,('温度制御','高温モード')],
#              [,('温度制御','節約モード')],
#              [,('温度制御','ミルクモード')],
#              [,('温度制御','センサ')],
#              [,('温度制御','状態表示')],
#              [,('温度制御','加熱')],
#              [,('温度制御方式','温度制御テーブル方式')],
#              [,('センサ','蓋センサ')],
#              [,('状態表示','沸騰ランプ')],
#              [,('状態表示','温度表示')],
#              [,('状態表示','モード表示')],
#              [,('水位検知','水位メータ')],
#              [,('水位検知','水位センサ')],
#              [,('エラー検知','高温エラー')]]

# print(sorted(cos_sim_l, reverse=True))

# i = 0
# cos_sim_para = []
# for l in cos_sim_l:
#     if cos_sim_l[i][0] >= 0.8:
#         cos_sim_para.append(l)
#         i = i + 1
#     else:
#         i = i + 1


# print(cos_sim_para)
        