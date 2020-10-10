https://leetcode.com/problems/word-break/

"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        if not s: return 0
        
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in words:
                print(w, s[i-len(w)+1:i+1])
                if w == s[i-len(w)+1:i+1] \
                	and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]
    
class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        if not s or not words:  return 0
        
        d = set(words)
        def dfs(s):
            if s in d:
                return 1
            for i in range(1, len(s)):
                pref = s[:i]
                suff = s[i:]
                if pref in d and not suff:
                    return 1
                if pref in d and dfs(suff):
                    return 1
            return 0
        return dfs(s)
        
# Word-break 2
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = set()
        wordDict = set(wordDict)
        def helper(word, op):
            nonlocal ans
            if not word:
                ans.add(op[:-1]) 
                return ""
            diff = op
            for i in range(len(word)):
                if word[:i + 1] in wordDict:
                    diff = helper(word[i + 1:], op + word[:i + 1]+ " ")
            return diff
                
        op = helper(s, "")
        return ans