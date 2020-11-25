# Suraj Pawar
from fractions import gcd
from functools import reduce
n = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
def calculate_lcm(a, b):
    # print((a*b)//gcd(a,b))
    return (a*b)//gcd(a,b)
lcm = reduce(calculate_lcm, a)

gcd = reduce(gcd, b)
temp = lcm
count = 0
while lcm <= gcd:
    if(gcd % lcm) == 0:
        count += 1
    lcm = lcm + temp
print(count)