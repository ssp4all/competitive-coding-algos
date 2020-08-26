https: // leetcode.com/problems/regular-expression-matching

"""
Given an input string (s) and a pattern (p), 
implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and 
characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
"""


class Solution:
    def isMatch(self, t: str, p: str) -> bool:
        if not p:
            return not t
        fm = bool(t) and p[0] in {'.', t[0]}

        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(t, p[2:]) or \
                (fm and self.isMatch(t[1:], p))
        else:
            return fm and self.isMatch(t[1:], p[1:])

# DP 
class Solution:
    def isMatch(self, t: str, p: str) -> bool:
        
        lt, lp = len(t), len(p)
        dp = [[0 for _ in range(lp + 1)] for _ in range(lt + 1)]
        dp[0][0] = 1

        for i in range(1, lp + 1):
            if "*" == p[i - 1]:
                dp[0][i] = dp[0][i - 2]

        for i in range(1, lt + 1):
            for j in range(1, lp + 1):
                if t[i - 1] == p[j - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == t[i - 1] or p[j - 2] == ".":
                        dp[i][j] |= dp[i - 1][j]
        # print(dp)
        return dp[-1][-1]
