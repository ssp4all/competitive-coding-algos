# https://leetcode.com/problems/valid-palindrome-ii

"""
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""

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