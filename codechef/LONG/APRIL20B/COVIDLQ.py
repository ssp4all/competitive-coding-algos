https://www.codechef.com/APRIL20B/submit/COVIDLQ

"""
3
3
1 0 1
7
1 0 0 0 0 0 1
11
0 1 0 0 0 0 0 1 0 0 1
"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    p = float('inf')
    flag = 0
    while i < n:
        if arr[i] == 1 and abs(p - i) < 6:
            flag = 1
            break
        elif arr[i] == 1:
            p = i 
        i += 1
    if flag:
        print("NO")
    else:
        print("YES")