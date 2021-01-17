import neologdn
import re

with open("sentence.txt") as f:
    text = f.read()

#全角・半角の統一と重ね表現の除去 (neologdn)
normalized_text = neologdn.normalize(text)

#URLの除去
text_without_url = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', normalized_text)

#桁区切りの除去と数字の置換
tmp = re.sub(r'(\d)([,.])(\d+)', r'\1\3', text_without_url)
text_replaced_number = re.sub(r'\d+', '', tmp)

# 半角記号の置換
tmp = re.sub(r'[!-/:-@[-`{-~]', r' ', text_replaced_number)

# 全角記号の置換 (ここでは0x25A0 - 0x266Fのブロックのみを除去)
text_removed_symbol = re.sub(u'[■-♯]', '、', tmp)

with open("sentence_after.txt", mode='w') as f:
    f.write(text_removed_symbol)
