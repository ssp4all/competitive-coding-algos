from math import sqrt
from functools import reduce
def find_factors(n):
	return set(reduce(list.__add__,
					([i, n//i] for i in range(1, int(sqrt(n)+1)) if not n%i)))
x = find_factors(285)
print(x)