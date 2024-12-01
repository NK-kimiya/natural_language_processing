text = '今度からMkDocksでドキュメントを書こう。#Python'

import  re

def clean_hashtag(text):
    clean_text = re.sub(r'#[a-zA-Z]+','',text)
    return  clean_text

print(clean_hashtag(text))
