n = int(input())
t = ()
t = list(t)
integer_list = map(int, input().split())
for i in integer_list:
    t.append(i)
t = tuple(t)
print(hash(t))