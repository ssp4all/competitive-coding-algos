# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        n = len(coins)
        ans = [float('inf')]*(amount+1)
        # print(ans)
        ans[0] = 0
        coins.sort(reverse=1)
        
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    ans[i] = min(ans[i], 1 + ans[i-coin])
        print(ans)
        return ans[-1] if ans[-1] != float('inf') else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 	 	   
		dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:   return -1 
        if not amount: return 0
        coins.sort()
        cache = {}
        def helper(amount):
            if amount in cache: return cache[amount]
            if amount < 0 or amount == 0:
                return 0
            else:
                mini = float('inf')
                for i in coins:
                    if i > amount:  break
                    mini = min(mini, helper(amount - i) + 1)
                cache[amount] = mini
                return mini
        x = helper(amount)
        return x if x != float('inf') else -1
        
        # coins.sort()
        # for i in range(n-1, -1, -1):
        #     if amount >= coins[i]:
        #         ans += amount // coins[i]
        #         amount = amount % coins[i]
        #     if  amount <= 0: break
        # print(amount, ans)
        # return ans if amount == 0 else -1

"""
Numbers of ways to form the amount
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @functools.lru_cache(None)
        def helper(amount, coins):
            if amount == 0: 
                return 1
            if amount < 0 or not coins:
                return 0
            return helper(amount - coins[-1], coins) + \
                        helper(amount, coins[:-1])

        return helper(amount, tuple(coins))
        
class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        dp = [0] * (amt + 1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amt + 1):
            
                if i >= c:
                    dp[i] += dp[i - c]
        return dp[-1]
