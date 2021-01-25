# MeCabモジュールのインポート
import MeCab
import unicodedata

# MeCab::Taggerクラスのインスタンスを作成（ここではデフォルト設定）
m = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')

#sentence = '鬼滅の刃の映画を見に行った。'
with open("sentence_after.txt") as f:
    text = f.read()

# 日本語文章の解析処理
ma = m.parse(text)

# 濁点処理
text = unicodedata.normalize('NFC', text)

# nouns = [line for line in m.parse(text).splitlines()
#                if "名詞" in line.split()[-1]]

nouns = [line.split()[0] for line in m.parse(text).splitlines()
               if "名詞" in line.split()[-1]]

# 重複削除
nouns_s = set(nouns)

# リスト化
nouns_l = list(nouns_s)

# for str in nouns_l:
#    print(str.split())

print(nouns_l)

# 解析結果を表示
#print(ma)