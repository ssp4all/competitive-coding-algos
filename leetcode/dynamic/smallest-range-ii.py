https://leetcode.com/problems/smallest-range-ii/

"""
Given an array A of integers, for each integer A[i] we need to choose either 
x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B
 and the minimum value of B.

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
"""

# O(nlgn)
class Solution(object):
    def smallestRangeII(self, A, K):
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans

# TC:O(2^n)
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        n = len(A)
        B = A[:]
        ans = float('inf')
        
        @functools.lru_cache(None)
        def backtrack(ind, mini, maxi):
            nonlocal ans
            if ind >= n:
                ans = min(ans, maxi - mini)
                return 

            for val in [K, -K]:
                B[ind] = A[ind] + val 
                backtrack(ind + 1, min(mini, B[ind]), max(maxi, B[ind]))
        
        backtrack(0, float('inf'), float('-inf'))
        return ans