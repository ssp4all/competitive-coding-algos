https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapp = {}
        for i, val in enumerate(order):
            mapp[val] = i
        return words == sorted(words, key=lambda x:tuple(mapp[i] for i in x))
        
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapp = {}
        for i, val in enumerate(order):
            mapp[val] = i
        # return words == sorted(words, key=lambda x:tuple(mapp[i] for i in x))
        
        def helper(s1, s2):
            if not s1 and not s2: return 1
            if s1 and not s2: return 0
            if not s1 and s2: return 1
            
            if mapp[s1[0]] < mapp[s2[0]]:
                return 1
            elif mapp[s1[0]] > mapp[s2[0]]:
                return 0
            else:
                return helper(s1[1:], s2[1:])
        
        n = len(words)
        i = 0
        while i < n-1:
            if helper(words[i], words[i+1]):
                i += 1
            else:
                return 0
        return 1