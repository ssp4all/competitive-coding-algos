https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""


# TC:O(lgN), SC:O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:    return [-1, -1]
        n = len(nums)
        
        def bsearch(tar, leftmost):
            l, r = 0, n - 1
            idx = -1
            while l <= r:
                m = (l + r) // 2 
                if nums[m] < tar:
                    l = m + 1 
                elif nums[m] > tar:
                    r = m - 1 
                else:
                    idx = m 
                    if leftmost:
                        r = m - 1 
                    else:
                        l = m + 1
            return idx 
        
        left = bsearch(target, True)
        right = bsearch(target, False)
        
        return [left, right]