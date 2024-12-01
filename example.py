from janome.tokenizer import Tokenizer
import os

# ユーザー辞書ファイルの絶対パスを取得
csv_path = os.path.abspath('userDict.csv')
print(csv_path)
# Tokenizerを初期化（ユーザー辞書を利用）
t = Tokenizer(udic=csv_path, udic_enc='utf8')

# 品詞分解する文章
text = '彼女と国立新美術館へ行った。'

# トークン化して表示
print("品詞分解結果：")
for token in t.tokenize(text):
    print(token)
