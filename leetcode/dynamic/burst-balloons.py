https://leetcode.com/problems/burst-balloons/

"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
 You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
 Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:    return 0 
        
        arr = [1] + nums + [1]
        n = len(arr)
        
        @functools.lru_cache(None)
        def helper(left, right):
            if left + 1 == right:   return 0 
            ans = 0
            for i in range(left + 1, right):
                ans = max(ans, arr[left] * arr[i] * arr[right] + helper(left, i) + \
                         helper(i, right))
            return ans

        return helper(0, n - 1)