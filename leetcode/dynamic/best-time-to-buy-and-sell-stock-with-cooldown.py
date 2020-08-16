"""
Say you have an array for which the ith element is the price of a 
given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions 
as you like (ie, buy one and sell one share of the stock multiple times) with the 
following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the 
stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:  return 0
        
        n = len(prices)
        
        if n <= 1:  return 0
        elif n == 2:
            if prices[0] < prices[1]:
                return prices[1] - prices[0]
            else:
                return 0
        dp = [[0, 0] for _ in range(n)]
        
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        dp[1][0] = max(dp[0][1] + prices[1], dp[0][0]) #sold
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1]) #buy
        
        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0]) #sold
            dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1]) #buy
        # print(dp)
        return dp[-1][0]
            