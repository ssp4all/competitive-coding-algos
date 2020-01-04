"""Check for whether string can be 
performed using permutation"""

def check_palindrome(s):
	ip = [0]*128
	count = 0
	for i in s:
		temp = ord(i) - ord('a')
		ip[temp] += 1
		if ip[temp] % 2 == 0:
			count -= 1
		else:
			count += 1
	return count <= 1

s = "aabbsd"
x = check_palindrome(s)
print(x)