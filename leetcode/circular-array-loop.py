https://leetcode.com/problems/circular-array-loop/
"""
You are given a circular array nums of positive and negative integers. 
If a number k at an index is positive, then move forward k steps. 
Conversely, if it's negative (-k), move backward k steps. 
Since the array is circular, you may assume that the last element's 
next element is the first element, and the first element's previous 
element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start 
and end at the same index and the cycle's length > 1. Furthermore, 
movements in a cycle must all follow a single direction. In other words, 
a cycle must not consist of both forward and backward movements.

Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
"""
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if not nums:    return 0
        for i, val in enumerate(nums):
            m = 3000 + i
            while nums[i] < 2000 and nums[i] * val > 0 and nums[i] % len(nums):
                val = nums[i]
                nums[i] = m
                i = (i + val) % len(nums)
            if nums[i] == m:
                return 1
        return 0
    