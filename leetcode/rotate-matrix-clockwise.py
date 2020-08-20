ip = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 3
k %= 4
if k == 1:
    new = zip(*ip)
    new = [row[::-1] for row in new] 
    print(new)
elif k == 2 or k == 3:
    new = ip[::-1]
    new = [row[::-1] for row in new] 
    print(new)
    if k == 3:
        new = zip(*new)
        new = [row[::-1] for row in new] 
        print(list(new))

#now merge
m = len(ip[0])
for i in range(m):
    for j in range(m):
        if i != j or i + j  != m - 1:
            ip[i][j] = new[i][j]

print(ip)