def itop(exp):

    def pred(x):
        if x == "/":    return 3
        elif x == "*":  return 2
        elif x in ["-", "+"]:   return 1
        else:   return 0

    s, op = [], []
    for i in exp:
        if i == " ":
            continue
        elif i == "(":
            s.append("(")
        elif i == ")":
            while s and s[-1] != "(":
                x = s.pop()
                op.append(x)
            s.pop()
        elif i in {"+", "-", "*", "/"}:
            while s and pred(s[-1]) >= pred(i):
                op.append(s.pop()) 
            s.append(i)
        else:
            op.append(i)
    while s:
        op.append(s.pop())
    print("".join(op))
ip = "2/3*3-2*3"
itop(ip)


# Basic calculator using infix to postfix

class Solution:
    def calculate(self, s):
        if not s:   return 0
        def operation(v1, v2, op):
            if op == "+":   return v1 + v2
            if op == "-":   return v2 - v1
            if op == "*":   return v1 * v2
            if op == "/":   return int(v2 / v1)
        
        prec = Counter({"/": 2, "*":2, "+":1, "-":1})
        def infix_to_postfix(s):
            st, op = [], []
            n = len(s)
            i = 0
            while i < n:
                if s[i] == " ":
                    i += 1
                    continue
                elif s[i] == "(":
                    st.append(s[i])
                elif s[i] == ")":
                    while st and st[-1] != "(":
                        op.append(st.pop())
                        i += 1
                    st.pop()
                elif s[i] in prec.keys():
                    # print
                    while st and prec[st[-1]] >= prec[s[i]]:
                        print("hit", st)
                        op.append(st.pop())
                    st.append(s[i])
                else:
                    temp = 0
                    while i < n and s[i].isdigit():
                        temp = temp * 10 + int(s[i])
                        i += 1
                    # i -= 1
                    op.append(temp)
                    continue
                i += 1
            while st:
                op.append(st.pop())
            # print(op)
            return op
        x = infix_to_postfix(s)
        # print(x) 
        nums = []
        
        for i in x:
            if str(i).isdigit():
                nums.append(i)
            else:
                n1, n2 = nums.pop(), nums.pop()
                temp = operation(n1, n2, i)
                nums.append(temp)
        return nums[-1]
                