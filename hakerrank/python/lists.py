n = int(input())
ip = []
for _ in range(n):
    name, *line = input().split()
    i = list(map(int, line))    
    if name == 'insert':
        ip.insert(i[0], i[1])
    elif name == 'print':
        print(ip)
    elif name == 'remove':
        ip.remove(i[0])
    elif name == 'append':
        ip.append(i[0])
    elif name == 'pop':
        ip.pop()
    elif name == 'reverse':
        ip.reverse()
    elif name == 'sort':
        ip.sort()
    else: 
        pass

