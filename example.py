with open('ja.text8','r',encoding='utf-8') as f:
    text = f.read()
    words = text.split()


from  collections import Counter
fdist = (Counter(words))
print(fdist.most_common(n=10))

