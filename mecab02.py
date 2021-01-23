from premecab import analysis_1, analysis_2

# 要求仕様書１
termlist1 = []
termlist2 = []
#newlist1 = []
#file1 = 'sentence_after.txt'
new_file1 = 'sentence_after_zu.txt'
print('パターン1:名詞+を抽出')
analysis_1(termlist1,new_file1)

print([t.word for t in termlist1])
print()

print(('パターン2:(名詞+)+(を、に、から、へ)+(サ変名詞OR動詞)を抽出'))
analysis_2(termlist2,new_file1)

print([t.word for t in termlist2])