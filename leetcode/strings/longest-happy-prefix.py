
https://leetcode.com/problems/longest-happy-prefix/


"""
A string is called a happy prefix if is a non-empty prefix which 
is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an 
empty string "" if no such prefix exists.

Example 1:

Input: s = "level"
Output: "l"
"""

# my bruteforce

class Solution:
    def longestPrefix(self, s: str) -> str:
        if not s:   return ""
        
        def getPrefix(s):
            prefs = set()
            for i in range(len(s)):
                prefs.add(s[:i])
            return prefs
        
        def getSuffix(s):
            suffs = set()
            for i in range(len(s) - 1, -1, -1):
                suffs.add(s[i:])
            return suffs
        
        prefs = getPrefix(s)
        suffs = getSuffix(s)
        return max(prefs & suffs, default="")