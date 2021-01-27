https://leetcode.com/problems/find-the-celebrity/discuss/71228/JavaPython-
O(n)-calls-O(1)-space-easy-to-understand-solution


def findTheCelebrity(n):
	if not n: return -1
	x = 0
	for i in range(n):
		if knows(x, i):
			x = i
	if any(knows(x, i) for i in range(n) if i != j):
		return -1
	if any(not knows(i, x) for i in range(n)):
		return -1
	return x
	
	"""
	[1, 1, 1]
	[0, 1, 0]
	[0, 1, 1]

	"""
