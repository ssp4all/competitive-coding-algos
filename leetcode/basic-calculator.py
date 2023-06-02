https://leetcode.com/problems/basic-calculator/

"""
Implement a basic calculator to evaluate
a simple expression string.

The expression string may contain open 
( and closing parentheses ), the plus + or minus sign -, 
non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3

"14-3/2"
"""

# Master-code
class Solution:
    def calculate(self, exp: str) -> int:
        n = len(exp)
        i = 0

        def pred(x):
            if x == "/":    return 3
            elif x == "*":  return 2
            elif x in ["-", "+"]:   return 1
            else:   return 0

        def operation(v1, v2, op):
            if op == "+":   return v1 + v2
            if op == "-":   return v2 - v1
            if op == "*":   return v1 * v2
            if op == "/":   return v2 // v1

        v, op = [], []
        while i < n:
            if exp[i] == " ":
                i += 1
                continue
            elif exp[i].isdigit():
                temp = 0
                while i < n and exp[i].isdigit():
                    temp = temp * 10 + int(exp[i])
                    i += 1
                i -= 1
                v.append(temp)
            elif exp[i] == "(":
                op.append(exp[i])
            elif exp[i] == ")":
                while op and op[-1] != "(":
                    v1, v2 = v.pop(), v.pop()
                    opr = op.pop()
                    ans = operation(v1, v2, opr)
                    v.append(ans)
                op.pop()
            else:
                while op and pred(op[-1]) >= pred(exp[i]):
                    v1, v2 = v.pop(), v.pop()
                    opr = op.pop()
                    ans = operation(v1, v2, opr)
                    v.append(ans)
                op.append(exp[i])
            i += 1 
            # print(i, op, v)
        while op and len(v) >= 2:
            v1, v2 = v.pop(), v.pop()
            opr = op.pop()
            ans = operation(v1, v2, opr)
            v.append(ans)
        if op and len(v) == 1:
            return v[-1] if op.pop() == "+" else v[-1]*-1
        return v[-1] if len(v) == 1 else "".join(map(str, v)) 

class Solution:
    def calculate(self, ss: str) -> int:
        if not ss:   return 0
        s = []
        ans = 0
        op = 0
        sign = 1
        for i in ss:
            if i == " ":
                continue
            elif i.isdigit():
                op = op * 10 + int(i)
            elif i in {"+", "-"}:
                ans += sign * op
                if i == "+":
                    sign = 1
                else:
                    sign = -1
                op = 0
            elif i == ")":
                ans += sign * op
                ans *= s.pop()
                ans += s.pop()
                op = 0
            elif i == "(":
                s.append(ans)
                s.append(sign)
                sign = 1
                ans = 0
        return ans + sign * op

https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s):
            s += '+0'
            stack, num, preOp = [], 0, "+"
            for i in range(len(s)):
                # print("->", s[i], stack)
                if s[i].isdigit(): num = num * 10 + int(s[i])
                elif not s[i].isspace():
                    if   preOp == "-":  stack.append(-num)
                    elif preOp == "+":  stack.append(num)
                    elif preOp == "*":  
                        print(stack)
                        stack.append(stack.pop() * num)
                    else:               stack.append((stack.pop() // num))
                    preOp, num = s[i], 0
            return sum(stack)


# solves all problems - basic I, II, and III
class Solution:
    def calculate(self, s):
        def update(op, v):
            if op == '+':   st.append(v)
            elif op == '-': st.append(-v)
            elif op == '*': st.append(st.pop() * v)
            elif op == '/': st.append(int(st.pop() / v))
        num, sign, i, st = 0, '+', 0, [] 
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-/*':
                update(sign, num)
                num, sign = 0, ch
            elif ch == '(':
                update(num, sign)
                num, j = self.calculate(s[i + 1: ])
                i = i + j
            elif ch == ')':
                update(sign, num)
                return sum(st), i + 1
            i += 1
        update(sign, num)
        return sum(st)