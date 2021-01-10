# MeCabモジュールのインポート
import MeCab

# MeCab::Taggerクラスのインスタンスを作成（ここではデフォルト設定）
m = MeCab.Tagger('')

sentence = '鬼滅の刃の映画を見に行った。'

# 日本語文章の解析処理
ma = m.parse(sentence)

# 解析結果を表示
print(ma)