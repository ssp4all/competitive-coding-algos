# Suraj Pawar
n = int(input().strip())
s = []
for k in range(n):
    arr.append(input().strip().split(" "))
[k, typ, cmptype] = input().strip().split(" ")
key = int(key) - 1
if cmptype == "lexicographic":
    s.sort(key=lambda x: x[key])
else:
    s.sort(key=lambda x: int(x[key]))
if typ == "true":#Tricky Part
    s.reverse()
for k in range(len(s)):
    print(" ".join(s[k]))