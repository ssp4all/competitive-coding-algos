# Suraj Pawar
# https://www.codechef.com/LTIME69B/problems/AVG
for _ in range(int(input())):
	n, k, v = map(int, input().split())
	ip = list(map(int, input().split()))
	
	x = ((v*(n+k)) - sum(ip))/k
	if x == int(x) and x>0:
		print(int(x))
	else:
		print('-1')