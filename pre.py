import neologdn

with open("sentence.txt") as f:
    text = f.read()

normalized_text = neologdn.normalize(text)

with open("sentence_after.txt", mode='w') as f:
    f.write(normalized_text)

#print(normalized_text)