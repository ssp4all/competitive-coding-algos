https://leetcode.com/problems/longest-harmonious-subsequence/

"""
We define a harmonious array as an array where the difference 
between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest
 harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from 
the array by deleting some or no elements without changing the
 order of the remaining elements.
"""
 
TC:O(N), SC:O(unique numbers)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        [1,3,2,2,5,2,3,7]
        [1,2,2,2,3,3,5,7 ]
        
        idea is to 
        1) count freq
        2) for each number ->
                    find freq of cur_num + freq of cur_num + 1
        3) return ans
        """
        freq = Counter(nums)
        res = 0
        
        for num in nums:
            if freq[num + 1] > 0:
                res = max(res, freq[num] + freq[num + 1]) 
        
        return res
