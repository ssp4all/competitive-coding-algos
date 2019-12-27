https://leetcode.com/problems/longest-palindromic-substring
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