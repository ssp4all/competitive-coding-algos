"""
4
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440
"""
t = int(input())
for tt in range(1, t + 1):
    r = int(input())
    ip = []
    for _ in range(r):
        ip.append(list(map(int, input().split())))
    c, j = [0, 0], [0, 0]
    ip.sort()
    # print(ip)
    flag = 0
    seq = []
    for i in ip:
        x, y = i
        # print(c, j)
        if not ((x < c[0] < y or x < c[1] < y) or \
                    (c[0] < x < c[1] or c[0] < y < c[1])):
            # print("C")
            c = i
            seq.append("C")
        elif not((x < j[0] < y or x < j[1] < y)or \
                    (j[0] < x < j[1] or j[0] < y < j[1])):
            j = i
            seq.append("J")
        else:
            print("Case #"+str(tt)+": IMPOSSIBLE")
            flag = 1
            break
    if not flag:
        print("Case #"+str(tt)+":"+"".join(seq))