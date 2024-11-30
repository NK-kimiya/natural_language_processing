#読み込み
with open('example.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)

#書き込み
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('Hello write method')
