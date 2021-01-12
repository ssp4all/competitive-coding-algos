def memoize(f):
	global memo
	memo = {}
	def helper(x):
		if x not in memo:            
			memo[x] = f(x)
		return memo[x]
	return helper
    

def fib(n):
	# print(memo)
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

fib = memoize(fib)

print(fib(10))
# memo = {}
print(memo)