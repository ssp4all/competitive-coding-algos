https://leetcode.com/problems/wildcard-matching/

"""
Given an input string (s) and a pattern (p), implement wildcard pattern 
matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*'
 matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p: return 1
        
        def helper(s, p):
            if s and not p:
                return 0
            if not s and not p:
                return 1
            if not s and p:
                if p[0] == "*":
                    return helper(s, p[1:])
                else:
                    return 0
        
            if p[0] == "?":
                return helper(s[1:], p[1:])
            elif p[0] == "*":
                return helper(s, p[1:]) or helper(s[1:], p)
            return s[0] == p[0] and helper(s[1:], p[1:])
        return helper(s, p)    

DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p: return 1
        dp = [[0 for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        
        dp[0][0] = 1
        
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 1]
                
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] in [s[i - 1], "?"]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # print(dp)
        return dp[-1][-1]
        