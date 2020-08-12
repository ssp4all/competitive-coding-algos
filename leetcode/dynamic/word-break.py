https://leetcode.com/problems/word-break/

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