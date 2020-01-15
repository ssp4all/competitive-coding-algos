https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        maxi = nums[0]
        for i in range(1, len(nums)):
            dp.append(nums[i] + [dp[i-1] if dp[i-1] > 0 else 0][0])
            maxi = max(maxi, dp[i])
        print(dp)
        return maxi

"""Optimized --> KADANE'S ALGORITHM""" 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	n = len(nums)
    	for i in range(1, n):
    		if nums[i-1] > 0:
    			nums[i] += nums[i-1]
    	return max(nums)
