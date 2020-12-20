import wn

def abstract_word(lemma):
    result1 = []
    for word in wn.getWords(lemma):
        for sense in wn.getSenses(word):
            if sense.src != 'hand': continue
            for synlink in wn.getSynLinks(sense, 'hype'):
                abst_sense = wn.getSense(synlink.synset2)
                if abst_sense and word.wordid != abst_sense.wordid:
                    result1.append(wn.getWord(abst_sense.wordid).lemma)
    return result1

words = wn.getWordsByLang()

def listout():
    result2 = []
    for word in words:
        lemma = word.lemma
        # print(lemma)

        for abst_word in abstract_word(lemma=lemma):
            result2.append((lemma,abst_word))
            # print([lemma,abst_word]) #(下位語、上位語)のタプル形式で出力

    return result2

with open('WordNet_list.txt', 'w') as f:
    print(listout(), file=f)

# print(listout()) # 日本語WordNetの下位上位概念を全て出力