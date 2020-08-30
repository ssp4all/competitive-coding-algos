# Suraj Pawar
def check(a,b):
	counter = 0
	while a != b:
		if b%a == 0:
			a *= 2
		elif a&1 == 1 and a != 1:
			a -= 1
			a >>= 1
		else:
			a >>= 1
		counter += 1
	print(counter)

for _ in range(int(input())):
	a, b = map(int, input().split())
	check(a, b)