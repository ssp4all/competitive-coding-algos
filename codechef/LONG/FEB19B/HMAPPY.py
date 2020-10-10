# Suraj Pawar
from fractions  import gcd
def LCM(a, b):
    return (int)(a*b)/gcd(a,b)
    
for _ in range(int(input())):
	n, a, b, k = map(int, input().split())
	pa = (int)(n/a)
	pb = (int)(n/b)
	lcm = LCM(a ,b)
	lcm = (int)(n/lcm)
# 	print(lcm)
	pa -= lcm 
	pb -= lcm
	if (pa+pb)>= k:
		print('Win')
	else:
		print('Lose')