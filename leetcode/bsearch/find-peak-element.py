https://leetcode.com/problems/find-peak-element/

"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
"""

class Solution:
    # TC: O(N)
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:    return 0
        l, cur = 0, 1
        n = len(nums)
        while cur < n and nums[l] <= nums[cur]:
            l += 1
            cur += 1
        return l
        
class Solution:
    # TC:O(lgN)
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:    return 0
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[m + 1]:
                r = m 
            else:
                l = m + 1
        return l
"""
[1,2,3,1]
[1,2,1,3,5,6,4]
[1]
"""