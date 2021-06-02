https://leetcode.com/problems/interleaving-string/

""" 
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a 
configuration where they are divided into non-empty substrings such that:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
"""

#TC:O(M*N), SC:O(M*N)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:    return 0 
        
        @functools.lru_cache(None)
        def same(i, j, k):
            if i == l1:
                return s2[j: ] == s3[k: ]
            if j == l2:
                return s1[i: ] == s3[k :]
            
            a = s1[i] == s3[k] and same(i + 1, j, k + 1)
            b = s2[j] == s3[k] and same(i, j + 1, k + 1)
            return a or b
            
        return same(0, 0, 0)