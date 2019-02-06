# code
n = int(input())
for _ in range(n):
    l = int(input())
    ip = []
    for _ in range(l):
        ip.append(input())
    counter = 0
    item = "".join(set(ip[0]))

    for z in item:
        if all(z in s for s in ip): 
            counter += 1
    print(counter)
