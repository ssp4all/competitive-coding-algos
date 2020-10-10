https://leetcode.com/problems/partition-equal-subset-sum/

"""
Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:    return 0
        sum_ = sum(nums)
        if sum_ & 1 == 1:   return 0
        n = len(nums)
        used = [-1] * n
        nums.sort()
        def bt(cur, st, temp_sum):
            if sum_//2 - temp_sum < 0: return 0
            if sum_//2 - temp_sum == 0: return 1
            for i in range(st, n):
                if used[i] == 1:    continue
                used[i] = 1
                if bt(cur + [nums[i]], i+1, temp_sum + nums[i]):
                    return 1
                used[i] = 0
            return 0
        
        if bt([], 0, 0):
            return 1
        return 0
#DP
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:    return 0
        tar = sum(nums)
        if tar & 1 > 0:    return 0
        
        def helper(nums, tar):
            dp = [0] * (tar + 1)
            dp[0] = 1
            for n in nums:
                for i in range(tar, n - 1, -1):
                    dp[i] += dp[i - n]
            # print(dp)
            return dp[-1]
        
        return helper(nums, tar //2)
