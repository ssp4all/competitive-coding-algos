

def min_meeting(ip):
	ans = 0
	end = []
	ip.sort()
	# print(ip)
	for i in ip:
		if len(end) != 0:
			if min(end) > i[0]:
				ans += 1
				end.append(i[1])
			else:
				end[end.index(min(end))] = i[1]
		else:
			end.append(i[1])
			ans += 1
	return ans



ip = [[1, 4], [5, 6], [8, 9], [2, 6]]
x = min_meeting(ip)
print(x)