# Suraj Pawar 
# https://www.codechef.com/FEB19B/problems/MAGICJAR
for _ in range(int(input())):
	n = int(input())
	ip = list(map(int, input().split()))
	for i in range(n):
		ip[i] -= 1
	print(sum(ip)+1) 