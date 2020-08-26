
Numbers of way to form a number N using K i.e.(1, 2, ...k)
def count(arr, k, n):
	if n == 0:
		return 1
	if n < 0:
		return 0
	if k <= 0 and n >= 1:
		return 0

	else return count(arr, k-1, n) + \
					count(arr, k, n-arr[k-1])
					