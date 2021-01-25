# MeCabモジュールのインポート
import MeCab
import unicodedata

def noun_extraction(text):
    m = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
    ma = m.parse(text)
    nouns = [line.split()[0] for line in m.parse(text).splitlines()
               if "名詞" in line.split()[-1]]
    # 重複削除
    nouns_s = set(nouns)

    # リスト化
    nouns_l = list(nouns_s)

