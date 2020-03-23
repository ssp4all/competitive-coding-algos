# Max possible meetings in a room


def max_meeting(ip):
	ans = 1
	ip.sort(key=lambda x: (x[1]))
    end = ip[0][1]
    n = len(ip)
    for i in range(1, n):
        if ip[i][0] > end:
            end = ip[i][1]
            ans += 1
    return ans
ip = [[1, 4], [5, 6], [8, 9], [2, 6]]
x = min_meeting(ip)
print(x)

# def min_meeting(ip):
	# ans = 0
	# end = []
	# ip.sort()
	# # print(ip)
	# for i in ip:
	# 	if len(end) != 0:
	# 		if min(end) > i[0]:
	# 			ans += 1
	# 			end.append(i[1])
	# 		else:
	# 			end[end.index(min(end))] = i[1]
	# 	else:
	# 		end.append(i[1])
	# 		ans += 1
	# return ans
# ip = [[1, 4], [5, 6], [8, 9], [2, 6]]
# x = min_meeting(ip)
# print(x)
