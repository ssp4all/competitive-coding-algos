https://leetcode.com/problems/4sum/

"""
Given an array nums of n integers and an integer target, are there elements 
a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:    return []
        
        nums.sort()
        # print(nums)
        n = len(nums)
        if n < 4:   return []
        if n == 4:  return [nums] if sum(nums) == target else []
        
        ans = set()
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                # if nums[j] == nums[j - 1]:  continue
                anchor, left, right = j, j + 1, n - 1
                while left < right:
                    tot = nums[i] + nums[anchor] + nums[left] +  nums[right]
                    if tot == target:
                        ans.add(tuple([nums[i], nums[anchor], nums[left], nums[right]]))
                        
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tot > target:
                        right -= 1
                    else:
                        left += 1
                
        return ans
"""
[-3,-2,-1,0,0,1,2,3]
0
[1,0,-1,0,-2,2]
0
[0,0,0,0]
0
"""