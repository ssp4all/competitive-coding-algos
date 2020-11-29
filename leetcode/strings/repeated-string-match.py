https://leetcode.com/problems/repeated-string-match/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not a or not b: return 0
        la = 0
        lb = len(b)
        
        if a.find(b) != -1:  return 1
        ans = 1
        org = a
        ll = len(org)
        while la + 1 < lb:
            a += org
            la += ll
            ans += 1
            if a.find(b) != -1: return ans
        return -1

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        la, lb = len(a), len(b)
        
        x = (lb - 1) // la + 1
        for i in range(2):
            if b in a*(x + i):
                return x + i
        return -1