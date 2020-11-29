https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # return 2 * sum(set(nums)) - sum(nums)
        
        if not nums: return -1
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == nums[m ^ 1]:
                l = m + 1
            else:
                r = m
        return nums[l]