
n = int(input())
op = input().split()
op = list(map(int, op))
op.sort( reverse = True)
# print(op)
for i in op:
    if i == max(op):
        pass
    else:
        break
    
print(i)
