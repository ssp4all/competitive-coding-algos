https://leetcode.com/problems/target-sum/

"""
You are given a list of non-negative integers, a1, a2, ..., an, and a 
target, S. Now you have 2 symbols + and -. For each integer, you should 
choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
"""

#Brute force
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:    return 0
        n = len(nums)
        cnt = 0
        def backtrack(cur, st, sum_):
            nonlocal cnt
            # print(cur)
            if sum_ == S:
                cnt += 1
            for i in range(st, n):
                cur[i] *= -1
                sum_ -= (2 * abs(cur[i]))
                backtrack(cur, i+1, sum_)
                sum_ += (2 * abs(cur[i]))
                cur[i] *= -1
        backtrack(nums, 0, sum(nums))
        return cnt


#DP
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:    return 0
        n = len(nums)
        sum_ = sum(nums)
        tar = (S + sum_)
        if S > sum_ or tar & 1 > 0:    return 0
        
        def helper(nums, tar):
            dp = [0] * (tar + 1)
            dp[0] = 1
            for n in nums:
                for i in range(tar, n - 1, -1):
                    dp[i] += dp[i - n]
            # print(dp)
            return dp[-1]
        
        return helper(nums, tar //2)