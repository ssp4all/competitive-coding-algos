# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return []
        n = len(nums)
        i = 0
        j = 0
        while j < n:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        while i < n:
            nums[i] = 0
            i += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return []
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            if nums[left] == 0:
                del nums[left] 
                nums.append(0)
                right -= 1
                left -= 1
            left += 1