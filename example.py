import  pandas as pd
json = pd.read_json('example.jsonl',lines=True,encoding='utf-8')
print(json)

