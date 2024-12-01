from  pathlib import  Path
p = Path('dir1')
print(list(p.glob('**/*.txt')))
