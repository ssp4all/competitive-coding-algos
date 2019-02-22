# Suraj Pawar
# https://www.codechef.com/COOK103B/problems/CHFPARTY
for _ in range(int(input())):
	ans = 0
	n = int(input())
	ip = list(map(int, input().split()))
	ip.sort()
	ans = ip.count(0)
	if ans == 0:
		print(0)
	else:
		for _ in range(ans):
			ip.remove(0)
		for i in range(len(ip)):
			if ip[i] <= ans:
				ans += 1
			else:
				break
		print(ans)