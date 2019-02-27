# Suraj Pawar
# https://www.codechef.com/COOK103B/problems/SECPASS
for _ in range(int(input())):
	n = int(input())
	ip = input()
	count = ip.count(ip[0])
	if count == 1:
		print(ip)
	else: 
		low = 1
		high = (n//count)+1
		i = 0
		while i<100:
			mid = (low+high)//2
			if low==high:
				break
			v = ip.count(ip[:mid])
			if v<count:
				high = mid
			else:
				low = mid
			if low+1==high:
				if ip.count(ip[:low])>ip.count(ip[:high]):
					mid = low
				else:
					mid = high
				break
			i+=1
		print(ip[:mid])