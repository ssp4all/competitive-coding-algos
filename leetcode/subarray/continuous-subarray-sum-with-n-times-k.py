https://leetcode.com/problems/continuous-subarray-sum/

"""
Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
"""

O(n^2)

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums: return 0
        n = len(nums)
        # if k == 0: return 0
        for i in range(n):
            sumi = 0
            for j in range(i, n):
                sumi += nums[j]
                if k == 0 and (j-i+1)>=2 and sumi == k:   return 1
                elif k != 0 and (sumi % k) == 0 and (j-i+1)>=2:
                    return 1
        return 0

optimal-> O(n)

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums: return 0
        n = len(nums)   
        sumi = 0
        dic = {0: -1}
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(n - 1))
        for i in range(n):
            sumi += nums[i]
            sumi = sumi % k
            if sumi in dic and (i-dic[sumi] > 1):
                return 1
            if sumi not in dic:
                dic[sumi] = i
        return 0
        