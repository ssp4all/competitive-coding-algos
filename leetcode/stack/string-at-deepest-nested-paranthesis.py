
"""
find string located in most nested parathesis 
input: ip = "(((ab)))((((abcd))))((cd))"
ans : 4 abcd

"""


ip = "(((ab)))((((abcd))))((cd))"
stack = []
string = ""
depth, cur = 0, 0
ans = ""
for ch in ip:
    if ch == "(":
        cur = 0
        string = ""
        stack += [ch]
    elif ch == ")":
        if stack:
            cur += 1
            if depth <= cur:
                depth = cur
                ans = string
            stack.pop()
        else:
            raise "Invalid Input!"
    else:
        string += ch
print(depth, ans)
