https://leetcode.com/problems/implement-strstr

class Solution:
    def strStr(self, s: str, pattern: str) -> int:
        if not s and not pattern: return 0
        if not pattern: return 0
        if not s: return -1
        n = len(s)
        l, r = 0, n-1
        temp = 0
        i = 0
        nn = len(pattern)
        while l <= r:
            if s[l-nn+1:l+1] == pattern:
                return l-nn+1
            if i >= nn:
                return -1
            if s[l] == pattern[i]:
                i += 1
            elif i> 0:
                l -= 1
                i = 0
            else:
                i = 0
            l += 1
                
        return -1

class Solution:
    def strStr(self, s: str, pattern: str) -> int:
        if not s and not pattern: return 0
        if not pattern: return 0
        if not s: return -1
        n, nn = len(s), len(pattern)
        for i in range(n-nn+2):
            if s[i:i+nn] == pattern:
                return i
        return -1