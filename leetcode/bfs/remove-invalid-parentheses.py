https://leetcode.com/problems/remove-invalid-parentheses/

"""
Remove the minimum number of invalid parentheses 
in order to make the input string valid. 
Return all possible results.

Note: The input string may contain letters other 
than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check(s):
            cnt = 0
            for i in s:
                if i == "(":
                    cnt += 1
                elif i == ")":
                    cnt -= 1
                if cnt < 0:
                    return 0
            return cnt == 0
        l = {s}
        while True:
            valid = []
            for j in l:
                if check(j):
                    valid.append(j)
            if valid:
                return valid
            ll = set()
            for s in l:
                for j in range(len(s)):
                    ll.add(s[:j] + s[j + 1:])
            l = ll
            # print(l)