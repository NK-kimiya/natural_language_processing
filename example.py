import string
import pandas as pd
import numpy as np

#テキストが日本語を含むかどうかを判定する
def filter_by_ascii_rate(text,threshold=0.9):
    ascii_letters = set(string.printable)
    rate = sum(c in ascii_letters for c in text) / len(text)
    return rate <= threshold

#指定されたデータセット（ファイル）を読み込み、日本語レビューとその評価（星の数）を抽出
def load_dataset(filename,n=5000,state=6):
    df = pd.read_csv(filename,sep='\t')
    
    is_jp = df.review_body.apply(filter_by_ascii_rate)
    df = df[is_jp]
    
    df = df.sample(frac=1, random_state=state)
    grouped = df.groupby('star_rating')
    df = grouped.head(n=n)
    return df.review_body.values,df.star_rating.values

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_and_eval(x_train,y_train,x_test,y_test,lowercase=False,tokenize=None,preprocessor=None):
    vectorizer = CountVectorizer(lowercase=lowercase,tokenizer=tokenize,preprocessor=preprocessor)
    x_train_vec = vectorizer.fit_transform(x_train)
    x_test_vec = vectorizer.transform(x_test)
    clf = LogisticRegression(solver='liblinear')
    clf.fit(x_train_vec,y_train)
    y_pred = clf.predict(x_test_vec)
    score = accuracy_score(y_test,y_pred)
    print('{:.4f}'.format(score))


