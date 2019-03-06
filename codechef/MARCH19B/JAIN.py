# Suraj Pawar
# https://www.codechef.com/MARCH19B/problems/JAIN
"""
1
3
aaooaoaooa
uiieieiieieuuu
aeioooeeiiaiei

"""
from itertools import combinations 
for _ in range(int(input())):
	n = int(input())
	ip = []
	for _ in range(n):
		ip.append(set(input()))
	print(ip)
	ip.sort(key=lambda x:len(x), reverse=True)
	print(ip)
	ans = 0
	for it in combinations(ip, 2):
		# print(it[0] | it[1])
		l = len(( it[0] | it[1]))
		if l < 2: break
		elif 5 == l:	ans += 1
	print(ans)
