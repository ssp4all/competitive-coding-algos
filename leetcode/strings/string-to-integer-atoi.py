https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        if not str: return 0
        n = len(str)
        op = 0
        start = 0
        flag = 0
        
        def check(op):
            op = op*-1 if flag else op
            if  op <= -2**31 :
                return -2**31
            elif op >= 2**31 - 1:
                return 2**31 - 1
            else:
                return op
        
        for val in str:
            if val.isdigit():
                start = 1
                if op != 0:
                    op *= 10
                    op += (ord(val) - ord("0"))
                else:
                    op += (ord(val) - ord("0"))
            elif start == 0 and val == "-":
                start = 1
                flag = 1
            elif start == 0 and val == "+":
                start = 1
                continue
            elif start == 0 and val == " ":
                continue
            else:
                break
        return check(op)