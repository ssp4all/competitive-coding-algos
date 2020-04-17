https://leetcode.com/problems/valid-parenthesis-string

class Solution:
    def checkValidString(self, s):
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0

   """Backtracking"""

        # def bt(s, cnt):
        #     print(s, cnt)
        #     if cnt < 0:
        #         return 0
        #     if cnt != 0 and not s:
        #         return 0
        #     if cnt == 0 and not s:
        #         return 1
        #     if s[0] == "(":
        #         cnt += 1
        #     elif s[0] == ")":
        #         cnt -= 1
        #     else:
        #         for c in ["(", "", ")"]:
        #             if c == "(":
        #                 cnt += 1
        #             elif c == ")":
        #                 cnt -= 1
        #             x = bt(s[1:], cnt)
        #             if x:
        #                 return 1
        #     x = bt(s[1:], cnt)
        #     if x:
        #         return 1
        # if bt(s, 0) == 1:   return 1
        # else:   return 0
       