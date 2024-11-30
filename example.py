import  pandas as pd
csv = pd.read_csv('example.csv',names=('name','grade'),header=None,encoding='utf-8')
print(csv)

