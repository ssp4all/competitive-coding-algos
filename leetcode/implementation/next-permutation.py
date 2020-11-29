https://leetcode.com/problems/next-permutation/

"""
Implement next permutation, which rearranges numbers into the lexicographically 
next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible 
order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums
        n = len(nums)
        # temp = nums[:]
        left = n - 2
        
        def reverse(ptr):
            r = n - 1
            while ptr < r:
                nums[ptr], nums[r] = \
                    nums[r], nums[ptr]
                r -= 1
                ptr += 1
        
        while left > -1:
            if nums[left] < nums[left + 1]:
                right = left + 1
                while right < n and nums[left] < nums[right]:
                    right += 1
                right -= 1
                nums[left], nums[right] = \
                    nums[right], nums[left]
                reverse(left + 1)
                return 
            left -= 1
        reverse(0)
        return 
            
