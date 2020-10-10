# Suraj Pawar
# https://www.codechef.com/MARCH19B/problems/CHDIGER
for _ in range(int(input())):
	n, d = map(int, input().split())
	ip = list(map(int, str(n)))
	count = len(ip)
	t = 0
	ans = []
	for i in ip:
		if i>=d:	t += 1
		else:
			while ans != [] and ans[-1]>i:
				ans.pop()
				t += 1
			ans.append(i) 
	temp = [d]*(count-len(ans))
	ans.extend(temp)
	ans = int("".join(map(str, ans)))
	print(ans)