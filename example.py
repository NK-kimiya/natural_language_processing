from janome.tokenizer import Tokenizer

# ストップワードを読み込む
try:
    with open('japanese-stopwords.txt', 'r', encoding='utf-8') as f:
        stopwords = set(w.strip() for w in f)
except FileNotFoundError:
    print("エラー: ストップワードファイルが見つかりません。")
    stopwords = set()

# ストップワードを除去する関数
def remove_stopwords(words, stopwords):
    return [w for w in words if w not in stopwords]

# テキストをトークン化して処理
t = Tokenizer(wakati=True)
text = 'りんごをいくつか買う。'
words = t.tokenize(text)
print("分かち書き結果:", words)

# ストップワードを除去
filtered_words = remove_stopwords(words, stopwords)
print("ストップワード除去後:", filtered_words)
print("ストップワードリスト:", stopwords)
print("'いくつか' in stopwords:", 'いくつか' in stopwords)
