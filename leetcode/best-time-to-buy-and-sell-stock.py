# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        ans = 0
        mini = 9999999999999999999
        n = len(prices)
        for i in range(n):
            mini = min(mini, prices[i])
            ans = max(ans, prices[i]-mini)
            
        return ans if ans> 0 else 0