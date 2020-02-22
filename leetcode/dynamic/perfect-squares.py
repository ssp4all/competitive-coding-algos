https://leetcode.com/problems/perfect-squares/

"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        if not n:   return 
        sq = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
        # print(sq)
        cache = {}
        def helper(m):
            if m in cache:  
                # print('hit')
                return cache[m]
            # print(m)
            if m in sq:
                return 1
            mini  = float('inf')
            
            for s in sq:
                if m < s:
                    break
                nn = helper(m - s) + 1
                mini = min(mini, nn)
            cache[m] = mini
            return mini
        return helper(n)

class Solution:
    def numSquares(self, n: int) -> int:
        if not n:   return 
        sq = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
        # print(sq)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for s in sq:
                print(i, s)
                if i < s:
                    break
                dp[i] = min(dp[i], dp[i-s] + 1)
        return dp[-1]