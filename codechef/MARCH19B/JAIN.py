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
	v = {}
	for _ in range(n):
		ip = "".join(sorted(set(input()))) 
		if ip in v:	v[ip] += 1
		else: v[ip] = 1
	# print(v)	
	ans = 0
	k = []
	for key in v.keys():
		k.append(key)
	# print(k)
	for it in combinations(k, 2):
		l = len(set( it[0] + it[1]))
		if 5 == l:	
			# print(it)
			ans += (v[it[0]]*v[it[1]])
	vowel = 'aeiou'
	if vowel in k:
		ans += (v[vowel]*(v[vowel]-1)) / 2
	
	print(int(ans))

# O(n*n)

# from itertools import combinations 
# for _ in range(int(input())):
# 	n = int(input())
# 	ip = []
# 	for _ in range(n):
# 		ip.append("".join(sorted(set(input()))))
# 	print(ip)
# 	ip.sort(key=lambda x:len(x), reverse=True)
# 	print(ip)

# 	ans = 0
# 	for it in combinations(ip, 2):
# 		print(it)
# 		l = len(set( it[0] + it[1]))
# 		if l <= 2: break
# 		elif 5 == l:	ans += 1
# 	print(ans)
