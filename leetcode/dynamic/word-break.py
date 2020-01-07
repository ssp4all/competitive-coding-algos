https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        if not s: return 0
        
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in words:
                print(w, s[i-len(w)+1:i+1])
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]
    