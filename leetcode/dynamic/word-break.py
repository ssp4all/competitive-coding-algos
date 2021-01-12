https://leetcode.com/problems/word-break/

# O(N^3)
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
# O(2^N)
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

# TC: O(N^3) SC: O(N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @functools.lru_cache(None)
        def dfs(s):
            if not s:   return 1
            for w in wordDict:
                if s.startswith(w):
                    if dfs(s[len(w):]):
                        return 1
            return 0
        return dfs(s)

# Word-break 2
"""
Given a non-empty string s and a dictionary wordDict containing a 
list of non-empty words, add spaces in s to construct a sentence 
where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
"""

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

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = set()
        cache = {}
        def helper(s):
            if not s:
                return []
            if s in cache:
                return cache[s]
            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(s) == len(word):
                    res += [word]
                else:
                    rest_of = helper(s[len(word):])
                    for item in rest_of:
                        item = word + " " + item
                        res += [item]
            cache[s] = res
            return res
        x = helper(s)
        return x

# better code for above
# TC: O(min(W, N) * 2^N)
# SC: O(2^N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:   return []

        @functools.lru_cache(None)
        def dfs(s):
            if not s:   return []
            
            res = []
            for w in wordDict:
                if not s.startswith(w): continue
                if len(w) == len(s):
                    res += [w]
                else:
                    restOf = dfs(s[len(w): ])
                    for item in restOf:
                        res += [w + " " +item]
            return res

        return dfs(s)