
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

"""
Template to solve most of the Stock related problems on LC
1) Find max profit from first transaction 
2) -"- from k transactions
"""

# TC:O(k*N), SC:O(K*N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if not prices:  return 0        

        count = 1 #at most 2 transactions
        
        dp = [[0 for _ in range(n)] for _ in range(count + 1)]
        
        for k in range(1, count + 1):
            mini = prices[0]
            for i in range(1, n):
                mini = min(mini, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - mini)
        return dp[-1][-1]

#########################################################
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not prices:  return 0 

        dp = [0] * n  
        
        mini = prices[0]
        for i in range(1, n):
            tmp = 0 if i < 2 else dp[i - 2]
            mini = min(mini, prices[i] - tmp)
            dp[i] = max(dp[i - 1], prices[i] - mini)
        return dp[-1]