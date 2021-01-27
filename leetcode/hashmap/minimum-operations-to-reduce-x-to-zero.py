https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

"""
You are given an integer array nums and an integer x. In one operation, 
you can either remove the leftmost or the rightmost element from the array 
nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's 
possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
"""


class Solution:
    # TC: O(N), SC:O(N)
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_ = sum(nums)
        target = sum_ - x 
        n = len(nums)
        if 0 == target:  return len(nums)
        # now maximize the length of subarray 
        seen = {0: -1} 

        res = float('-inf')
        
        sum_ = 0
        for i in range(n):
            sum_ += nums[i]
            if sum_ - target in seen:
                res = max(res, i - seen[sum_ - target])
            seen[sum_] = i
        return -1 if res == float('-inf') else n - res
    
    # TC: O(N^2 * x), SC:O(N^2 * x)
    def minOperations(self, nums: List[int], x: int) -> int:
        if not x:   return 1 
        
        @functools.lru_cache(None)
        def helper(l, r, x):
            if (not (l <= r) and x > 0) or (x < 0):   return float('inf')
            if x == 0:  return 0
            return 1 + min(helper(l + 1, r, x - nums[l]), 
                      helper(l, r - 1, x - nums[r]))
        
        steps = helper(0, len(nums) - 1, x)
        return steps if steps != float('inf') else -1
    