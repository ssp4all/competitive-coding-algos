def dec_to_bin(n):
	if n>1:
		dec_to_bin(n//2)
	print(n%2, end="")

def dec_to_bin(n):
	return bin(n).replace("0b", "")

def bin_to_dec(n):
	return int(n, 2)

def bin_to_dec(n):
	s = str(n)
	n = len(s)
	num = 0
	# print(s, n)
	for i in range(n-1, -1, -1):
		if int(s[i]) != 0:
			# print('yea')
			num += pow(2, n-i-1)
	print(num)

	
bin_to_dec(1111)
