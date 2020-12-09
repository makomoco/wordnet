import wn

def abstract_word(lemma):
    result = []
    for word in wn.getWords(lemma):
        for sense in wn.getSenses(word):
            if sense.src != 'hand': continue
            for synlink in wn.getSynLinks(sense, 'hype'):
                abst_sense = wn.getSense(synlink.synset2)
                if abst_sense and word.wordid != abst_sense.wordid:
                    result.append(wn.getWord(abst_sense.wordid).lemma)
    return result

words = wn.getWordsByLang()

for word in words:
    lemma = word.lemma
    print(lemma)

    for abst_word in abstract_word(lemma=lemma):
        print('-', abst_word)
