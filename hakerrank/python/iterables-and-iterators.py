# Suraj Pawar
from itertools import combinations

n = int(input())
ip = list(input().strip().split())
t = int(input())

c = list(combinations(ip, t))
d = filter(lambda x: 'a' in x, c)
print('{0:.3}'.format(len(list(d))/len(c)))