# https://leetcode.com/problems/longest-palindromic-substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        n = len(s)
        ans = ""
        for i in range(n):
            for j in range(i+1, n+1):
                ss = s[i:j]
                if ss == ss[::-1]:
                    if j-i > len(ans):
                        ans = ss
        return ans

"""Dynamic Progr"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        n = len(s)
        ans = 1
        start = 0
        dp = [ [0 for _ in range(n)] for _ in range(n)]
        for i in range(n): #single char
            dp[i][i] = 1
        for j in range(0, n-1): #double char
            if s[j] == s[j+1]:
                dp[j][j+1] = 1
                start = j
                ans = 2
        #3 or more than 3 chars
        k = 3
        while k <= n:
            i = 0
            while i < (n - k + 1):
                j = i + k - 1
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    if k > ans:
                        ans = k
                        start = i
                i += 1
            k += 1
        return s[start: start + ans ]
                
        
"""Cheking left and right"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        n = len(s)
        ans = ""
        for c in range(2*n - 1):
            l = c // 2
            r = l + c % 2
            while l>=0 and r<n and s[l] == s[r]:
                ss = s[l:r+1]
                if len(ans) < len(ss):
                    ans = ss
                l -= 1
                r += 1
        return ans