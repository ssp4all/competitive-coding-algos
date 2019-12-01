# https://leetcode.com/problems/most-common-word/
class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        d = dict()
        p = p.translate(str.maketrans(',', ' ', "!?';."))         
        p = p.split()
        print(p)
        for i in p:  
            i = i.lower()
            if i not in banned:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1 
        print(d)
        x = max(d.keys(), key=lambda x: d[x])
        return x