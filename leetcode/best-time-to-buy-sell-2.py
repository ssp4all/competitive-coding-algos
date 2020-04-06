Best Time to Buy and Sell Stock II

"""
Say you have an array for which the ith 
element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions 
at the same time (i.e., you must sell the stock before 
you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on 
day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on 
day 5 (price = 6), profit = 6-3 = 3.
"""


from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not prices or n == 1:  return 0
        b = prices[0]
        s, p = prices[0], 0
        for i in range(n - 1):
            if prices[i + 1] >= prices[i]:
                s = max(s, prices[i + 1])
            else:
                p += (s - b)
                b = prices[i + 1]
                s = b
                b = min(b, prices[i + 1])
            # print(s, b)
        p += (s - b)
        return p
        
# class Solution {
#     public int maxProfit(int[] prices) {
#         int maxprofit = 0;
#         for (int i = 1; i < prices.length; i++) {
#             if (prices[i] > prices[i - 1])
#                 maxprofit += prices[i] - prices[i - 1];
#         }
#         return maxprofit;
#     }
# }