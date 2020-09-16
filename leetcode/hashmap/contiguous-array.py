https://leetcode.com/problems/contiguous-array/

"""
Given a binary array, find the maximum length of a contiguous subarray with 
equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:    return 0
        n = len(nums)
        cache = {0: -1}
        c = 0
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                c -= 1
            else:
                c += 1
            if c in cache:
                ans = max(ans, i - cache[c])
            else:
                cache[c] = i
        return ans
        
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         # print(nums[i:j])
        #         sub = nums[i:j]
        #         if sub.count(0) == sub.count(1):
        #             ans = max(ans, j - i)
        # return ans