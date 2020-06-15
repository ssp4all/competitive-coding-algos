https://leetcode.com/problems/largest-divisible-subset/

"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) 
of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:    return nums
        dp = [[]]
        for n in sorted(nums):
            dp += [(max((s+[n] for s in dp if not s or n % s[-1] == 0), key=len))]
            # print(dp)
        return max(dp, key=len)