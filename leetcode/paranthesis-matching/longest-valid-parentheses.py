https://leetcode.com/problems/longest-valid-parentheses/

"""
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:   return 0
        n = len(s)
        
        maxi = 0
        def is_valid(s, i, maxi):
            count = 0
            for j in range(i, len(s)):
                if s[j] == "(":    count += 1
                else:  count -= 1
                if count < 0:   break
                if count == 0:
                    maxi = max(maxi, j - i + 1)
            return maxi
        
        for i in range(n):
            maxi = max(maxi, is_valid(s, i, maxi))
            if maxi >= n - i + 1:
                break
        return maxi

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:   return 0
        n = len(s)
        
        st = [-1]
        maxi = 0
        for i in range(n):
            if s[i] == "(": st += [i]
            else:
                st.pop()
                if not st:   st += [i]
                else:   maxi = max(maxi, i - st[-1])
            # print(maxi)
        return maxi