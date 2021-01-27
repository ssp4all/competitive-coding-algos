https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away

"""
Given an array nums of 0s and 1s and an integer k, return True if 
all 1's are at least k places away from each other, otherwise return False.

Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
"""

# TC:O(N), SC:O(1)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        try:
            anchor = nums.index(1, )
        except: 
            anchor = -1
        if anchor == -1 or k == 0:    return 1
        n = len(nums)
        
        for i in range(anchor + 1, n):
            if nums[i] == 1:
                if i - anchor - 1 < k:
                    return 0
                anchor = i
        return 1