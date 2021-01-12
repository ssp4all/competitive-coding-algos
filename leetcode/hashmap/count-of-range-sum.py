
https://leetcode.com/problems/count-of-range-sum/

"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
"""

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1]+n)
        record = collections.defaultdict(int)        
        res = 0
        for csum in cumsum:
            for target in range(lower,upper+1):
                if csum - target in record:
                    res += record[csum - target]
            record[csum] +=1
        return res