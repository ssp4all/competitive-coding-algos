https://leetcode.com/problems/number-of-equivalent-domino-pairs/

"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
"""
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        if n == 0:  return 0
        
        seen = defaultdict()
        ans = 0
        for a, b in dominoes:
            num = min(a, b) * 10 + max(a, b)
            if num in seen:
                ans += seen[num]
                seen[num] += 1
            else:
                seen[num] = 1
        return ans