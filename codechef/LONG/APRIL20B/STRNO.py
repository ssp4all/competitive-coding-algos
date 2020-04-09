https://www.codechef.com/APRIL20B/problems/STRNO

# Suraj Pawar
1
4 2

from math import sqrt
for _ in range(int(input())):
    x, k = map(int, input().split())

    def soe(n):
        f = 0
        while n % 2 == 0:
            n //= 2
            f += 1
        
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                f += 1
                n //= i
        if n > 2:
            f += 1
        return f

    ans = soe(x)
    if ans >= k:
        print(1)
    else:
        print(0)