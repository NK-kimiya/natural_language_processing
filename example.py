from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter

text = '彼女と国立美術館へ言った。'
token_filters = [POSKeepFilter('名詞')]
a = Analyzer(token_filters=token_filters)
for token in a.analyze(text):
    print(token)