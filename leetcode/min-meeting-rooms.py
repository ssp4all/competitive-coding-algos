def min_lec(lec):
	n = len(lec)
	prefix = [0]*20
	for i in range(n):
		prefix[lec[i][0]] += 1
		prefix[lec[i][1] + 1] -= 1
	print(prefix)
	ans = prefix[0]

	for i in range(1, 20):
		prefix[i] += prefix[i-1]
		ans = max(ans, prefix[i])
	print(ans)

lec = [[ 0, 5 ], [ 1, 2 ], [ 1, 10 ]]
min_lec(lec)
