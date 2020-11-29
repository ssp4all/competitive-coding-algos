https://www.codechef.com/problems/SQRDSUB

# Suraj Pawar
for _ in range(int(input())):
    n = int(input())
    ip = list(map(int, input().split()))
    temp = []
    for i in range(n):
        if ip[i] & 1:
            temp += [0]
        else:
            if ip[i] % 4 == 0:
                temp += [2]
            else:
                temp += [1]
    d = {0:1}
    cur, ans = 0, 0
    for t in temp:
        cur += t
        if (cur - 1) in d:
            ans += d[(cur - 1)]
        d[cur] = d.get(cur, 0) + 1
    total = (n * (n + 1)) // 2
    print(total - ans)  