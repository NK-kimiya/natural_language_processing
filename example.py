import  pandas as pd
csv = pd.read_csv('example.tsv',encoding='utf-8',sep='\t')
print(csv)

csv_2 = pd.read_table('example.tsv',encoding='utf-8')
print((csv_2))

