from collections import defaultdict
d=defaultdict(int)
d['a']=1
d['b']=2
d['c']=3
print(d['a'])
print(d['d'])
## in normal dictionary would raise key error but in default dict it will return default value of int which is 0