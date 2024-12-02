with open('ja.text8','r',encoding='utf-8') as f:
    text = f.read()
    words = text.split()


from  collections import Counter
fdist = (Counter(words))

UNK='<UNK>'
PAD='<PAD>'
vocab = {PAD: 0,UNK: 1}
for word, _ in fdist.most_common():
    vocab[word] = len(vocab)

words = ['私','は','元気']
word_ids = [vocab.get(w,vocab[UNK]) for  w in  words]
print(word_ids)