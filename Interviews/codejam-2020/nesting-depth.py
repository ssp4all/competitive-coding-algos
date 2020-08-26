"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

For example, in the following strings, all digits 
match their nesting depth: 0((2)1), (((3))1(2)), ((((4)))), ((2))((2))(1). 
The first three strings have minimum length among those that have the same 
digits in the same order, 
but the last one does not since ((22)1) also has the digits 221 and is shorter.

"""

for tt in range(1, int(input())+1):
    s = str(input())
    n = len(s)
    op = 0
    ans = []
    for i in range(n): 
        if op < int(s[i]):
            t = (int(s[i]) - op)
            ans.extend(["("* t])
            op += t
            ans.append(s[i])
        elif op == int(s[i]):
            ans.append(s[i])
        else:
            t = op - int(s[i])
            ans.extend([")" * t])
            op -= t
            ans.append(s[i])
    ans.extend([")" * op])
    print("Case #"+str(tt)+": "+"".join(ans))
