"""
Given an array of citations (each citation is a non-negative integer) of a researcher, 
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of 
his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
"""

import collections
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        n = len(citations)
        citations.sort()
        ans = 0
        res = 0
        for ind in range(n - 1, -1, -1):
            ans += 1
            if citations[ind] >= ans:
                res += 1
        return res

import collections
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        n = len(citations)
        cache = collections.defaultdict(int)
        for i in range(n):
            if citations[i] >= n:
                cache[n] += 1
            else:
                cache[citations[i]] += 1
        tot = 0
        for i in range(n, -1, -1):
            tot += cache[i]
            if tot >= i:
                return i 
        return 0