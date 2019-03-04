# Suraj Pawar
# https://www.codechef.com/MARCH19B/problems/JAIN
from itertools import combinations 
for _ in range(int(input())):
	n = int(input())
	ip = []
	for _ in range(n):
		ip.append(set(input()))
	op = list(combinations(ip, 2))
	temp = []
	for i in range(len(op)):
		temp.append(op[i][0].union(op[i][1]))
	ans = 0
	for j in temp:
		if 5 == sum(list(map(str(j).count, "aeiou"))):	
			ans += 1
	print(ans)
