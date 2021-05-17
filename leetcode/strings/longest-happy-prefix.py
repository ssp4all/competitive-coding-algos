
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
# TC:O(N*N), SC:O(N*N)
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

#upsolving 

"""
uses idea of rolling hashing 
eg, s = "abc"

for prefix, 
h[a] = a 
h[b] = a * 128 + b 
h[c] = a * 128 ^ 2 + b * 128 ^ 1 + c 

for suffix, 
h[c] = c 
h[bc] = c + b * 128 ^ 1 
h[abc] = c + b * 128 ^ 1 + a * 128 ^ 2 

see, h[abc] == h[abc]
"""

# TC: O(N), SC:O(1)
class Solution:
    def longestPrefix(self, s: str) -> str:
        if not s:   return ""
        
        res = 0 
        l, r = 0, 0 
        MOD = 10 ** 9 + 7
        
        for i in range(len(s) - 1):
            
            #prefix hash 
            l = (l * 128 + ord(s[i])  ) % MOD 
            
            #suffix hash 
            r = (r + pow(128, i, MOD) * ord(s[~i])) % MOD 
            
            if l == r:  res = i + 1
        
        return s[: res]