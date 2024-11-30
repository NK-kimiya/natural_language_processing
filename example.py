import  pandas as pd
csv = pd.read_csv('example.csv',encoding='utf-8')
print(csv)
print(csv['grade'])
