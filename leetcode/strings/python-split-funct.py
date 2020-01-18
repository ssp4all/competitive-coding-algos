""" 
Inplace reversal without any inbuilt functions
"""
s = "welcome you are"
ss = list(s)
print(ss)
n = len(ss)
def reverse_str(str, l, r):
    while l < r:
        str[l], str[r] = str[r], str[l]
        l += 1
        r -= 1
    return str
ss = reverse_str(ss, 0, n-1)
print(ss)
l = 0
ss += [" "]
print(ss)
for i in range(n+1):
    if ss[i] == " ":
        ss = reverse_str(ss, l, i-1)
        l =  i +  1
        print("l-> ", l)
print(ss[:-1])


ss = "i love you ::"
s = list(ss)
n = len(ss)
cur = n
s.append('@')
i = 0
op = []

while i < n:
	tmp = ""
	while i < n and s[i] != " ":
		if s[i] == "@":	break
		tmp += s[i]
		i += 1
	s.append(tmp)
	if s[i] == "@": break
	n += 1
	i += 1
print(s[cur+1:])