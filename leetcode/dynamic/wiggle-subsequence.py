https://leetcode.com/problems/wiggle-subsequence/

"""
A wiggle sequence is a sequence where the differences between successive 
numbers strictly alternate between positive and negative. The first 
difference (if one exists) may be either positive or negative. A 
equence with fewer than two elements is trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the 
differences (6, -3, 5, -7, 3) are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle 
sequences, the first because its first two differences are positive 
and the second because its last difference is zero.
A subsequence is obtained by deleting some elements 
(eventually, also zero) from the original sequence, 
leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
"""

# TC:O(N), SC:O(N)

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        diff = [prev - curr for prev, curr in zip(nums, nums[1:]) if prev != curr]
        peak = sum(prev * curr < 0 for prev, curr in zip(diff, diff[1:]))
        return peak + 2 if any(diff) else int(bool(nums))