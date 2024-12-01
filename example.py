from  janome.tokenizer import Tokenizer
text='彼女と国立美術館へ行った。'
t = Tokenizer(wakati=True)
for token in t.tokenize(text):
    print(token)
