https://leetcode.com/problems/word-pattern
from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not str and not pattern: return 0
        ss = str.split(" ")
        if len(ss) != len(pattern): return 0
        x = {}
        temp = 1
        ip1, ip2 = [], []
        for i in ss:
            if i not in x:
                x[i] = temp
                temp += 1
            else:
                ip1.append(x[i])
        temp = 1
        y = {}
        for i in pattern:
            if i not in y:
                y[i] = temp
                temp += 1
            else:
                ip2.append(y[i])

        return ip1 == ip2
                
        
        