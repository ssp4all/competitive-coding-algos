https://leetcode.com/problems/concatenated-words

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words or not words[0]:
            return []
        d = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
                pref = word[:i]
                suff = word[i:]
                if pref in d and suff in d:
                    return 1
                if pref in d and dfs(suff):
                    return 1
                
            return 0
        
        op = []
        for word in words:
            if dfs(word):
                op.append(word)
        return op


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words or not words[0]:
            return []
        words.sort(key=lambda t:len(t))
        d = set()
        def dfs(w):
            if not d:   return 0
            if w in d:  return 1
            for i in range(1, len(w)):
                if w[:i] in d and dfs(w[i:]):
                    return 1
            return 0
        res = []
        for w in words:
            if dfs(w):
                res.append(w)
            d.add(w)
        return res