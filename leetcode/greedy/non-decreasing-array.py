https://leetcode.com/problems/non-decreasing-array/


""" 
Given an array nums with n integers, your task is to check 
if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] 
holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

Input: nums = [4,2,3]
Output: true
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if not nums:    return 1 
        
        wrong = 0 
        n = len(nums)
        
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                wrong += 1
                if i - 2 < 0 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return wrong <= 1
