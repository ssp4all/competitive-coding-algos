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