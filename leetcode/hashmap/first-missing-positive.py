https://leetcode.com/problems/first-missing-positive/

"""
Given an unsorted integer array, 
find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if not nums:    return 1
        
        nums += [0]
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        
        for i in range(n):
            nums[ nums[i] % n ] += n
            
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n