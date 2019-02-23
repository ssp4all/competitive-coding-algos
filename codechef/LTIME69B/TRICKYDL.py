# Suraj Pawar
# https://www.codechef.com/LTIME69B/problems/TRICKYDL
for _ in range(int(input())):
	a = int(input())
	i = 0
	pt = []
	while True:
		i += 1
		p = (a*i)-((2**i)-1)
		if p < 0:	
			break
		pt.append(p)
	d1 = i-1
	d2 = pt.index(max(pt))
	print(d1, int(d2+1), sep=' ')	