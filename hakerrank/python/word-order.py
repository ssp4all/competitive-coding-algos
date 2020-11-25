# Suraj pawar
from collections import Counter
n = int(input())
ip=[]
for i in range(n):
    ip.append(input())
count = Counter(ip)
print(len(count))
print(*count.values())
