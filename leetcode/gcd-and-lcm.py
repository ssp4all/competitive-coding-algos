def gcd(a, b):
	if not a or not b: return a or b
	else: return gcd(b%a, a)

def lcm(a, b):
	return (a*b) / gcd(a, b)

"""GCD for list"""
from fractions import gcd
from functools import reduce
def find_gcd(list):
    x = reduce(gcd, list)
    return x

x = gcd(10, 90)
print(x)