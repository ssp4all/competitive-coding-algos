https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or not k:   return 0
        tar, rem = divmod(sum(nums) , k)
        if rem:     return 0
        nums.sort()
        
        def helper(grps):
            if not nums:    return 1
            x = nums.pop()
            for i, grp in enumerate(grps):
                if grp + x <= tar:
                    grps[i] += x
                    if helper(grps):    return 1
                    grps[i] -= x
                if not grp:    break
            nums.append(x)
            return 0
        
        if nums[-1] > tar:  return 0
        while nums and nums[-1] == tar and k:
            # print(nums)
            nums.pop()
            k -= 1
        # print(nums)
        return helper([0] * k)

For two subsets

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:    return 0
        k = 2
        tar, rem = divmod(sum(nums), k)
        if rem:     return 0
        nums.sort()
        
        def helper():
            if not nums: return 1
            x = nums.pop()
            for i, val in enumerate(arr):
                if val + x <= tar:
                    arr[i] += x
                    if helper():    return 1
                    arr[i] -= x
                if not val: break
            nums.append(x)
            return 0
                
        
        while nums and nums[-1] == tar and k:
            nums.pop()
            k -= 1
        
        arr = [0] * k
        return helper()
            