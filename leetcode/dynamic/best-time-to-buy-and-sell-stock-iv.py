https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., 
you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
"""

Brute force

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:  return 0
        
        profits = set()
        
        for idx, buy in enumerate(prices):
            for jdx, sell in enumerate(prices):
                if jdx > idx and sell - buy > 0:
                    profits.add((idx, jdx, sell - buy))

        def isvalid(comb):
            # check for overlapping combination
            comb = list(comb)
            comb.sort(key=lambda x:x[0])
            for i in range(len(comb) - 1):
                if comb[i][1] >= comb[i + 1][0]:
                    return 0
            return 1

        profit = 0
        for i in range(1, k + 1):
            for comb in itertools.combinations(profits, i):
                if isvalid(comb):
                    profit = max(profit, sum(stock[2] for stock in comb))
        return profit