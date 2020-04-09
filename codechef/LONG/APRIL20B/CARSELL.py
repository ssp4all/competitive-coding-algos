https://www.codechef.com/APRIL20B/submit/CARSELL

# Suraj Pawar
"""
2
3
6 6 6
3
0 1 0
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=1)
    amt = 0
    for i in range(n):
        t = (arr[i] - i) 
        if t < 0:
            break
        amt += (t % (10**9 + 7))
    amt %= (10**9 + 7)
    print(amt)
