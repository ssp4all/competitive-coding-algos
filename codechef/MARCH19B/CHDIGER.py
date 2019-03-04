# Suraj Pawar
# https://www.codechef.com/MARCH19B/problems/CHDIGER
for _ in range(int(input())):
	n, d = map(int, input().split())
	# op = 0
	# for c in str(n):
	# 	if int(c)>=d:
	# 		op += 1
	# print(op)
	r = max([int(c) for c in str(n)])
	if r<d:
		print(n)
	else:
		# n = int(n)	
		while d<r:
			r = max([int(c) for c in str(n)])
			n = int(n)*10 + d
			n = str(n).replace(str(r), "", 1)
		print(int(n))