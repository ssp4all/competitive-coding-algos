# Suraj Pawar
# https://www.codechef.com/MARCH19B/problems/CHNUM
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	pos, neg = [], []
	for i in range(n):
		if a[i] > 0:
			pos.append(a[i])
		else:
			neg.append(a[i])
	lpos = len(pos)
	lneg = len(neg)
	mx = max(lpos, lneg)
	mi = min(lpos, lneg)
	if mx == n or mi == n:
		mx, mi = n, n
	print(mx, mi)