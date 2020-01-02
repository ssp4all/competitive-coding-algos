https://leetcode.com/problems/maximum-product-of-word-lengths

"""Brute force"""
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words: return 0
        n = len(words)
        ans = 0
        # maxi = -99*99
        def isMismatch(a, b):
            if not len(set(a).intersection(set(b))):
                return 1
            else: 
                return 0
            
        for i in range(n):
            for j in range(1, n):
                a, b = words[i], words[j]
                if isMismatch(a, b):
                    ans = max(ans, len(a)*len(b))
        return ans