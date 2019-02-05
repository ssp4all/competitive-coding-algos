# cook your dish here
# Suraj Pawar
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))
    flag = 0
    for i in range(n):
        if i == 0:
            if (a[n-1]+a[i+1]) < d[i]:
                flag = 1
                break
        elif i == (n-1):
            if (a[i-1]+a[0]) < d[i]:
                flag = 1
                break
        elif (a[i-1]+a[i+1]) < d[i]:
            flag = 1
            break	
    if flag == 0:
        print('-1')
    else:
        print(d[i])