https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:   return 0
        l = 0
        def helper(s, l):
            if not s:
                return l
            elif len(s) == 1:
                l += 1
                return l
            elif s[0] == s[-1]:
                l += 2
                return helper(s[1 : -1], l)
        
            else:
                l = max(helper(s[1:], l), helper(s[:-1], l))
                return l
        l = helper(s, 0)
        return l


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:   return 0
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s[-j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]