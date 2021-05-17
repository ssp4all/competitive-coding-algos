https://leetcode.com/problems/delete-operation-for-two-strings/


"""
Given two strings word1 and word2, return the minimum
 number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.


Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
"""

# TC:O(M*N), SC:O(M*N)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        #solve like a LCS 
        @functools.lru_cache(None)
        def helper(word1, word2):
            if not word1 or not word2:  return 0 
            res = 0
            if word1[0] == word2[0]:
                res = 1 + helper(word1[1:], word2[1:])
            else:
                res = max(helper(word1[1:], word2), \
                         helper(word1, word2[1:]))
            return res 
        
        return len(word1) + len(word2) - 2 * helper(word1, word2)