https://leetcode.com/problems/min-cost-climbing-stairs/

"""
On a staircase, the i-th step has some non-negative cost 
cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. 
You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost += [0]
        cache = {}
        def helper(n):
            if n in cache:  return cache[n]
            if n in [0, 1]: return cost[n]
            x = cost[n] + min(helper(n - 1), helper(n - 2))
            cache[n] = x
            return x
        return helper(len(cost) - 1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        ans = [0] * (n + 1)
        for i in range(2, n+1):
            ans[i] = min(cost[i - 1] + ans[i - 1],
                            cost[i - 2] + ans[i - 2])
        return ans[-1]