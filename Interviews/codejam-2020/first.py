t = int(input())
for tt in range(1, t + 1):
    d = int(input())
    r = {i:set() for i in range(d)}
    c = {i:set() for i in range(d)}
    
    dia = 0
    rc = {i:0 for i in range(d)}
    cc = {i:0 for i in range(d)}
    # print(rc, cc)
    ip = []
    for i in range(d):
        ip.append(list(map(int, input().split())))
    #print(ip)
    for i in range(d):
        for j in range(d):
            if i == j:
                dia += ip[i][j]
            if not rc[i] and ip[i][j] in r[i]:
                rc[i] = 1
            if not cc[j] and ip[i][j] in c[j]:
                cc[j] = 1
            r[i].add(ip[i][j])
            c[j].add(ip[i][j])
    print("Case #"+str(tt)+":",dia, sum(rc.values()),sum(cc.values()))