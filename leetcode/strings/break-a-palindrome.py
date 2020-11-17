https://leetcode.com/problems/break-a-palindrome/

"""
Given a palindromic string palindrome, replace exactly one character 
by any lowercase English letter so that the string becomes the 
lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.

Example 1:
Input: palindrome = "abccba"
Output: "aaccba"
"""


class Solution:
    def breakPalindrome(self, S: str) -> str:
        for i in range(len(S) // 2):
            if S[i] != 'a':
                return S[:i] + 'a' + S[i + 1:]
        return S[:-1] + 'b' if S[:-1] else ''