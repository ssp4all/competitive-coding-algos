# Suraj Pawar
# https://www.codechef.com/submit/ARTBALAN
for _ in range(int(input())):

	ip = list(input())
	n = len(ip)
	freq = [0]*26
	# print(freq)
	for i in range(n):
		freq[ord(ip[i])-ord('A')] += 1
	# print(freq, ip)
	freq.sort()
	# print(freq)
	ans = 99999999999999999
	for i in range(1,27):
		if n%i != 0:
			continue
		bal_no = n/i
		total, repetition = 0, 0
		for j in range(1,i+1):
			total += abs(freq[26-j] - bal_no)
			repetition += freq[26-j]
		ans = min((n-repetition+total)/2, ans)
	print(int(ans))