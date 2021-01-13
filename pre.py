import neologdn

with open("sentence.txt") as f:
    text = f.read()

normalized_text = neologdn.normalize(text)

print(normalized_text)