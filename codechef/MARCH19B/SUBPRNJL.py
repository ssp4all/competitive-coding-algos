# Suraj Pawar
# https://www.codechef.com/MARCH19B/problems/SUBPRNJL
"""
1
3 3
1 2 3
"""
from math import ceil
for _ in range(int(input())):
	n, k = map(int, input().split())
	ip = []
	ip = list(map(int, input().split()))
	# print(ip)
	a = 1
	index = []
	for i in range(n): 
		for j in range(n-i): 
			index.append([j,a+j-1])
		a += 1
	print(index)
	b = []
	# print(k)
	for i in range(len(index)):
		m = ceil(k / ( index[i][1]
						-index[i][0]
							+1))
		
		b.append(m)
		# print(m)
	print(b)

	x = [sorted(ip[index[i][0]:(index[i][1]+1)]*b[i])[k-1] for i in range(len(index))]
	print(x)
		
	f = [ip[index[i][0]:(index[i][1]+1)].count(x[i]) for i in range(len(x))]
	# print(f)
	bs = 0
	for i in range(len(f)):
		if f[i] in ip[index[i][0]:(index[i][1]+1)]:
			bs += 1
	print(bs)
