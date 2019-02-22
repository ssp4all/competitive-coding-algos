# Suraj Pawar
# https://www.codechef.com/COOK103B/problems/TABLET
for _ in range(int(input())):
	n, b = map(int, input().split())
	ip = []
	for  _ in range(n):
		ip.append(list(map(int, input().split())))
	area = [] 
	for i in range(n):
		if ip[i][2] <= b:
			a = ip[i][0] * ip[i][1]
			area.append(a)
	if area != []:
		print(max(area))
	else:
		print('no tablet')