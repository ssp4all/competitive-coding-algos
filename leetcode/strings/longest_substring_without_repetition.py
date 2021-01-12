# https://leetcode.com/problems/longest-substring-without-repeating-characters

"""
Given a string s, find the length of the longest substring without 
repeating characters. 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        temp = []
        n = len(s)
        for i in range(n):
            while temp and s[i] in temp:
                temp.pop(0) 
            temp.append(s[i])
            ans = max(ans, len(temp))
        return ans

"""Optimized """
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st, ml = 0, 0
        used = {}
        for i, c in enumerate(s):
            if c in used and st <= used[c]:
                st = used[c] + 1
            else:
                ml = max(ml, i-st+1)
            used[c] = i
        return ml