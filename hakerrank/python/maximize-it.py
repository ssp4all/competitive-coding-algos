from itertools import product

K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x) % M, product(*N))
print(max(results))

# Suraj Pawar
k, m = map(int, input().split())
ip = []
op = []
for _ in range(k):
    n, *i = map(int, input().split())
    ip.append(list(i))
total = 0
for j in ip:
    maxi = 0
    for k in j:
        if maxi < (k**2) % m:
            maxi = k**2
    op.append(maxi)
for i in op:
    total += i
print(int(total % m))
