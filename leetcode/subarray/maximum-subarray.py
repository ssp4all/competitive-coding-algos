https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        maxi = nums[0]
        for i in range(1, len(nums)):
            dp.append(nums[i] + [dp[i-1] if dp[i-1] > 0 else 0][0])
            # dp[i] += (nums[i] + max(dp[i - 1], 0))
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


"""Circular subarray sum """
class Solution:
    def maxSubarraySumCircular(self, a: List[int]) -> int:
        # if not a:   return 0
        tot, curMax, maxi, curMin, mini = 0, 0, float('-inf'), 0, float('inf')
        for i in a:
            tot += i
            curMax = max(curMax + i, i)
            maxi = max(maxi, curMax)
            curMin = min(curMin + i, i)
            mini = min(mini, curMin)
        return max(maxi, tot - mini) if maxi > 0 else maxi
            