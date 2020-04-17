https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        op = []
        st = []
        # print(s)
        for ind, i in enumerate(list(s)):
            # print(i)
            if i == "(":
                st += [ind]
            elif i == ")":
                if not st:
                    op += [ind]
                else:
                    st.pop()
        op += st
        # print(op, st)
        x = "".join([j for i, j in enumerate(s) if i not in op])
        # print(x)
        return x