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