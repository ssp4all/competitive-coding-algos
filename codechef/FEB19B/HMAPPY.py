# cook your dish here
# Suraj Pawar- ssp4all
t = int(input())
for _ in range(t):
	n, a, b, k = map(int, input().split())
	pa, pb = 0, 0
	for i in range(1,n+1):
		if i%a == 0 and i%b == 0:
			continue
		elif i%a == 0 and i%b != 0:
			pa += 1
		elif i%b == 0 and i%a != 0:
			pb += 1
	if (pa+pb) >= k:
		print('Win')
	else:
		print('Lose')