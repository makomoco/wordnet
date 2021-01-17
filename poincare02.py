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
# major_occupation_list = ['性別','種別']
major_occupation_list = ['話題 沸騰 ホ ゚ット GOMA 型 要求 仕様 書 ', '版 ', '胡麻 印 ', 'ほうひ ゙ん株 ', 'ト ゙キュメント ', 'こ ゙利用 ', '著作 物 ',
                         '著作 権 ', '作成 者 ', '所属 ', '組織 ', '゙所有 ', '著作 権 法 ', '保護 ', 'SESSAME ', '著作 者 ', '利用 ', '許諾 ',
                         '゙利用 者 個人 ', '使用 許諾 ', '使用 ', '個人 以外 ', '方 ', '゙', '場合 ', 'query sessame jp ', '゙お問い合わせ ', '゙さい',
                         '゙著作 者 ', '権利 著作 物 ', '複製 ', '上演 ', '演奏 ', '公衆 送信 及 ', '゙送信 可能 化 ', '口述 ', '展示 ', '上映 及 ', '゙頒布 ',
                         '貸与 ', '翻訳 ', '翻案 ', '二 次 的 著作 物 ', '目次 ', '機能 要件 ', 'ハート ゙ウェア 構成 ', '操作 ハ ゚ネル 部 ', '温度 制御 方式 ',
                         '温度 制御 仕様 ', 'エラー 検知 ', 'システム ', '動作 ', '制約 事項 ', '今回 設計 ', '沸騰 ホ ゚ット ', 'ユーサ ゙に以下 ', '機能 ', '提供 ',
                         '家電 製品 ', '゙す', '•ホ ゚ット 内 ', '水 ', '沸騰 ', '保温 ', '給湯 ', '•ユーサ ゙が指定 ', '時間 ', '゙きたら', 'フ ゙サ ゙ー ', 'キッチン タイマ 機能 ',
                         '以降 ', '章 ', 'ホ ゚ット ', '要求 ', '詳細 ', '説明 ', 'ハート ゙ウェア 構成 対象 ', '以下 ', 'よう ', '外観 ', '蓋 操作 ハ ゚ネル ', '給湯 口 ', '取手 ',
                         '貯水 部 ', '断熱 性 ', 'ステンレス 素材 ', 'ため ', 'ホ ゚ット 内 ', '゙きるようになっています', '内部 ', '構成 ', 'ホ ゚ンフ ゚', '水路 ', '蓋 センサ ',
                         '満水 センサ 給水 線 ', '水位 センサ ', 'サーミスタヒータ 用 電源 ', 'ヒータ ', 'ここ ', '用語 ', '意味 ', '次 ', 'とおり ', '•満水 センサ ', '水位 ',
                         '許容 上限 ', '゙うかを検出 ', 'セン ', 'サ ', '゙on ', '時 ', '゙許容 上限 ', 'こと ', '•', 'n 水位 センサ ', '検出 ', 'センサ ', 'on ', '位置 ', 'す ',
                         '•蓋 センサ ', '蓋 ', '゙ている時 ', '•サーミスタ ', '水温 ', '•ヒータ ', '加熱 ', '•ヒータ 用 電源 ', '電力 ', '供給 ', '通常 ', '異常 ', '゙発生 ', 'off ',
                         '遮断 ', '•給水 線 ', 'ユーサ ゙', '゙できる水量 ', '上限 ', '目印 ', '満水 センサ ', '若干 下 ', '•ホ ゚ンフ ゚', '上 ', '゙て', '排出 ', '•水路 ', 'ホ ゚ンフ ゚によって',
                         '゙られる水 ', '通路 ', '操作 ハ ゚ネル 部 ホ ゚ット 上部 ', '操作 ハ ゚ネル ', 'ランフ ゚', '温度 モート ゙表示 窓 ', 'タイマ 分 ', '沸騰 保温 水位 ', '温度 ', '高温 節約 ミルク ',
                         '解除 ロック ', '保温 設定 ', 'タイマ 残り 時間 表示 窓 ', '•タイマホ ゙タン ', '水位 メータ ', 'ホ ゙タン ', 'タイマ ', '゙起動 ', '回 ', '毎 ', '追加 ', '•タイマ 残り 時間 表示 窓 ',
                         'タイムアッフ ゚までの残り 時間 分 単位 ', '切り 上 ', '゙表示 ', '•保温 設定 ホ ゙タン ', '保温 モート ゙', '高温 °C 保温 ', '節約 °C 保温 ', 'ミルク °C 保温 モート ゙', '設定 ', '高温 ',
                         '節約 ', 'ミルク ', 'モート ゙が', '•温度 モート ゙表示 窓 現在 ', '保温 モート ゙図 中 ', '•解除 ホ ゙タン 給湯 口 ', 'ロック 解除 ', 'ロック 中 ', '給湯 ホ ゙タン ', 'ロック ', '解除 ',
                         '給湯 中 ', '゙きません', '•ロックランフ ゚給湯 口 ', '゙ロック ', '゙う', '点灯 ', '•給湯 ホ ゙タン ', '間中 ', '手 ', '停止 ', '•沸騰 ホ ゙タン ', 'カルキ 抜き ', '沸騰 中 ', '中止 ', 
                         '保温 状態 ', '•沸騰 ランフ ゚水 ', '゙終了 ', '消灯 ', '•保温 ランフ ゚沸騰 中 ', '゙ない時 ', '沸騰 ホ ゙タン 押下 等 ', '゙水 ', '•水位 メータホ ゚ット 内 ', '表示 ', '関係 ', '対応 ', 
                         'インシ ゙ケータセル ', '複数 ', '呼 ', '゙れるランフ ゚により構成 ', '数 ', '同数 ', 'セル ', '゙on 状態 ', '時 水 ', '゙あると検出 ', '゙点灯 ', '例 ', '間 ', 'on off ', '制御 ', '制御 方式 ',
                         '制御 周期 ', '操作 量 ', '下図 ', '゙操作 量 ', '゙けヒータ ', '上記 ', '決定 ', '方式 ', '゙あります', 'PID 制御 方式 ', '温度 特性 ', '比例 係数 Kp ', '微分 係数 Kd ', '積分 係数 Ki ',
                         '式 ', '゙時間 t ', '操作 量 M ', '゙計算 ', '目標 温度 Tg ', '⊿T ', 'E ', 'T T ', 'T ', 't ', 'M E Kp E Ki ∫Edt Kd dE dt 水温 °C ', '数式 ', '展開 ', '前回 ', '今回 ', '差 ⊿M ',
                         '⊿M M M Kp T T Ki Tg T Kd T T T ', 'の ', 'M M ⊿M ', '゙し', '≦M ≦', '温度 制御 テーフ ゙ル 方式 ', '図 ', 'あら かし ゙め', 'テーフ ゙ル ', '保存 ', '操作 量 決定 時 ', '参照 ', 'E °C ',
                         '≧≦', '⊿T °C ≧', '≦', '目標 温度 ON OFF 方式 ', '温度 上昇 中 ', '目標 温度 ', '温度 下降 中 ', 'ヒータ on 時 ', 'ヒータ off 時 ', '水温 °C ', 'off on ', '境 ', 'ヒステリシス ', '方法 ',
                         '温度 T ', 'off on off on ', '仕様 ', '゙られた場合 温度 制御 可能 ', '゙沸騰 状態 ', '移行 ', '゙°C ', '後 ', '分間 加熱 ', 'その後 保温 状態 ', '温度 制御 ', '操作 量 算出 ', '目標 温度 ON OFF 方式 ヒステリシス ', '適用 ', '分 ', '沸騰 状態 ', '場合 高温 モート ゙が設定 ', '°C ', '場合 節約 モート ゙が設定 ', '場合 ミルクモート ゙が設定 ', '沸騰 ホ ゙タン 押下 ', '強制 沸騰 ', '制御 仕様 ', '同様 ', '保温 設定 ホ ゙タン ', '変更 ', '場合 移行 ', '仕様 毎 ', '操作 量 算出 方法 ', '機種 ', '゙故障 誤動作 ', 'エラー ', '検知 ', 'これ ', '異常 過熱 ', '火災 等 ', '危険 ', '回避 ', 'サーミスタ ', '故障 ', 'ソフトウェア ', '゙はエラー ', '゙きないため', 'ハート ゙ウェア 的 ', '断線 ', '安全 ', '確保 ',
                         '及 ', '゙ホ ゚ンフ ゚', '故障 誤動作 ', '設計 ', 'もの ', '種類 ', '分類 ', '゙できます', '高温 エラー ', '゙停止 ', '゙きなくなった場合 ', '発生 ', 'ヒータ 用 電源 ', '秒 間 フ ゙サ ゙ー ', '高温 エラー 検知 ', 
                         '温度 上 ', '゙らずエラー これ ', '゙動作 ', '゙不安定 ', 'ヒータ 制御 中 ', '一定 周期 ', '゙水温 ', '゙°C 下 ', '゙り', '前回 検出 ', '今回 検出 ', '水温 検出 周期 ', '最初 ', '°C 水温 ', '゙すが', 
                         '今回 検出 温度 前回 検出 温度 ', '゙エラー ', '番 目 ', '゙温度 上 ', '゙らずエラー ', '水温 °C 目標 温度 ', '今回 検出 温度 ', '前回 検出 温度 ', 'b 温度 上 ', '゙ない例 ', '今回 検出 温度 エラー 検知 ', 
                         'c 温度 上 ', '゙検知 ', 'システム 全体 ', '動作 仕様 ', '゙なりません', '゙off ', '゙可能 ', 'それ 以外 ', '沸騰 ホ ゙タン ', '•蓋 ', 'とき ', '沸騰 ランフ ゚及 ', '゙保温 ランフ ゚は消灯 ', '•保温 モート ゙', '際 ', 
                         '゙なかった場合 ', '必 ', '゙一 度 沸騰 ', '自然 ', 'なか ゙ら設定 温度 ', '•タイマ ', '最大 時間 ', '゙設定 ', '゙きます', '•ユーサ ゙', 'ホ ゙タン タイマ ', '制約 時 ', '•ユーサ ゙が設定 ', 'タイム アウト 時 ', 
                         '゙沸騰 状態 終了 時 ', '•T B D ', 'ハート ゙ウェア ', '要件 ', '゙確定 ', '゙T B D ', '要求 仕様 書 ', '教育 用 資料 ', '環境 ', '適宜 ', '制約 ', '゙いて結構 ', '発行 履歴 ', 
                         '話題 沸騰 ホ ゚ット GOMA 型 要求 仕様 書 年月日 初版 発行 ', '年月日 ', '版 発行 ']
figure_title = ''
iplot(poincare_2d_visualization(model, relations_set, figure_title, num_nodes=None, show_node_labels=major_occupation_list))