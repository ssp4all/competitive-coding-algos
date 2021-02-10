
https://leetcode.com/problems/missing-number/

"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space 
complexity and O(n) runtime complexity?

nums = [3,0,1]
Output: 2
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        return int(((n+1)*n)/2) - sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:    return 0 
        n = len(nums)
        
        tot = 0
        for i in range(n):
            tot = tot ^ i ^ nums[i]
        
        return tot ^ n