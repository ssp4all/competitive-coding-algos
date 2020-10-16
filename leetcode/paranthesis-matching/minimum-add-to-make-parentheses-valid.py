https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:   return 0
        n = len(s)
        
        count = 0
        ans = 0
        for ch in s:
            if ch == "(":   count += 1
            else:   count -= 1
            if count < 0:
                ans += 1
                count = 0
        return ans + abs(count)