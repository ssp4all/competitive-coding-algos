# https://leetcode.com/problems/repeated-substring-pattern
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s: return False
        n = len(s)
        for i in range(1):
            for j in range(i, n//2):
                x = s[i:j+1]
                # print(x)
                l = len(x)
                if n % l == 0 and n // l != 1:
                    q = n // l
                    if x*q == s:
                        # print(x, q)
                        return True
        return False

""" optimized """
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s: return False
        temp = (s*2)[1:-1]
        return temp.find(s) != -1