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
            
# https://leetcode.com/problems/next-greater-element-iii/
class Solution:
    def nextGreaterElement(self, n: int) -> int:
            
        """
        Idea is to be 
        - Use same logic as used in Next Permutation
        - N = 230241 -> ANS is 230412
        - N = 2,3,0,2,4,1
        - first, find bigger number to right number sequence 
        - second, find just bigger number on the right
        - finally, reverse the sequence on the right of fisrt found number
        - Return it!
        """
        
        nums = list(str(n))
        size = len(nums)
        # if size == 1:   return n 
        
        right = size - 2
        
        def reverse(nums, l, r):
            while l < r:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1 
                r -= 1
        
        while right >= 0:
            if int(nums[right]) < int(nums[right + 1]):
                left = right + 1
                while left < size and int(nums[left]) > int(nums[right]):
                    left += 1
                left -= 1
                nums[left], nums[right] = nums[right], nums[left]
                
                reverse(nums, right + 1, size - 1)
                ans = int("".join(nums)) 
                return ans if ans <= 2**31 - 1 else -1
            right -= 1
                
                
        return -1