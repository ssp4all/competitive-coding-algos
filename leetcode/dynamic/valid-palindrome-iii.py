https://leetcode.com/problems/valid-palindrome-iii/

"""
Given a string s and an integer k, find out if the given 
string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a 
palindrome by removing at most k characters from it.

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
"""

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        def helper(s, k):
            print(s, k)
            if not s:
                return 1
            if k == 0:
                return s == s[::-1]
            elif k < 0:
                return 0
            if s[0] == s[-1]:
                return helper(s[1:-1], k)
            else:
                return helper(s[1:], k - 1) or helper(s[:-1], k - 1)
        return helper(s, k)

Dynamic programming approach
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s[-j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return n - dp[-1][-1] <= k
        