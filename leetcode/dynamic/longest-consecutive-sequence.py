https://leetcode.com/problems/longest-consecutive-sequence/

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:    return 0
        n = len(nums)
        nums.sort()
        op = 0
        ans = float('-inf')
        for i in range(n - 1):
            diff = nums[i+1] - nums[i] 
            if diff == 1:
                op += 1
                ans = max(ans, op+1)
            elif diff == 0:
                continue
            else:
                op = 0
        return ans if ans != float('-inf') else 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:    return 0
        n = len(nums)
        nn = set(nums)
        ans, temp = 0, 0
        for i in range(n):
            temp = 1
            st = nums[i]+1
            while st in nn:
                st += 1
                temp += 1
            ans = max(ans, temp)
            temp = 1
            st =  nums[i] - 1
            while st in nn:
                st -= 1
                temp += 1
            ans = max(ans, temp)
        return ans

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:    return 0
        nums = set(nums)
        ans = 0
        for i in nums:
            if i - 1 in nums: continue
            c = 1
            st = i + 1
            while st in nums:
                st += 1
                c += 1
            
            ans = max(ans, c)
        return ans