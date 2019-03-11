# Suraj Pawar
# https://www.codechef.com/MARCH19B/problems/SUBPRNJL
"""
1
3 3
1 2 3
"""
for _ in range(int(input())):
	n, k = map(int, input().split())
	ip = []
	# for i in range(n):
	ip = list(map(int, input().split()))
	print((ip))
	# Subarray generation
	a = []
	k = 1
	for i in range(n): 
		for j in range(n-i): 
			a.append(ip[j:k+j]) 
		k += 1
	print(a)
