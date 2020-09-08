https://leetcode.com/problems/distinct-subsequences/

"""

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It's guaranteed the answer fits on a 32-bit signed integer.

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)
"""	

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def recur(s, t):
            if not s or not t:
                return int(not t)
            count = recur(s[1:], t)
            if s[0] == t[0]:
                count += recur(s[1:], t[1:])
            return count
        
        return recur(s, t)

 #memo
 class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def recur(s, t):
            if (s, t) in cache: return cache[(s, t)]
            if not s or not t:
                return int(not t)
            count = recur(s[1:], t)
            if s[0] == t[0]:
                count += recur(s[1:], t[1:])
            cache[(s, t)] = count
            return count
        
        return recur(s, t)

#DP
ls, lt = len(s), len(t)
        dp = [[0 for _ in range(ls + 1)] for _ in range(lt + 1)]
        
        for i in range(ls + 1):
            dp[0][i] = 1
        
        for i in range(lt):
            for j in range(ls):
                if s[j] == t[i]:
                    dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[-1][-1]