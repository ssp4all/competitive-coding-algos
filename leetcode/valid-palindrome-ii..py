# https://leetcode.com/problems/valid-palindrome-ii

class Solution(object):
    def validPalindrome(self, s):
        if not s: return 1
        n = len(s)
        l, r = 0, n-1
        while l < r:
            if s[l] != s[r]:
                t, tt = s[l: r], s[l+1: r+1]
                return t == t[::-1] or tt == tt[::-1]
            l += 1
            r -= 1
        return 1            