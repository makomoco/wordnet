# MeCabモジュールのインポート
import MeCab

# MeCab::Taggerクラスのインスタンスを作成（ここではデフォルト設定）
m = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')

#sentence = '鬼滅の刃の映画を見に行った。'
with open("sentence.txt") as f:
    text = f.read()

# 日本語文章の解析処理
ma = m.parse(text)

# 解析結果を表示
print(ma)