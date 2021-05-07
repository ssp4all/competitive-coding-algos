https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, nums: List[int], tar: int) -> List[List[int]]:
        if not nums:    return []
        n = len(nums)
        ans = set()
        def bt(temp, remain, st):
            if remain < 0:
                return
            elif remain == 0:
                ans.add(tuple(temp))
            else:
                for i in range(st, n):
                    bt(temp + [nums[i]], remain - nums[i], i)
                    
        bt([], tar, 0)
        return ans


# https://leetcode.com/problems/combination-sum-iv
"""
Given an array of distinct integers nums and 
a target integer target, return the number of 
possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
"""


#TC:O(N), SC:O(N)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:    return 0 
        nums.sort()
        
        #this is basically coin-change 
        ans = 0
        
        @functools.lru_cache(None)
        def recur(amt):
            if amt < 0: return 0 
            if amt == 0:    
                return 1
            ways = 0
            for num in nums:
                if num > amt:   continue 
                ways += recur(amt - num)
            return ways
        
        return recur(target)