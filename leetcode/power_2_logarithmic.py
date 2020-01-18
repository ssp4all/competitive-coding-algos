def power(n):
	if n == 0:
		return 1
	elif n == 1:
		return 2
	else:
		x = power(n//2)
		if n % 2 != 0:
			return 2*x*x
		else:
			return x*x
	# return x
x = power(6)
print(x)

