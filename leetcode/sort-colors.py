# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lo = m = 0
        hi = n - 1
        while m <= hi:
            if nums[m] == 0:
                nums[lo], nums[m] = nums[m], nums[lo]
                lo += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[hi], nums[m] = nums[m], nums[hi]
                hi -= 1
                