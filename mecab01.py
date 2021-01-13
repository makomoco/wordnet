from parser import MecabParser

mp =  MecabParser(word_classes=['名詞'], word_class_details=['一般','固有名詞'])
text = '今日はお腹が空いたので近所の天下一品のラーメンを食べに来ました。'
print(mp.parse(text))