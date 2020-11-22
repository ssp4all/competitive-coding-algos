https://leetcode.com/problems/degree-of-an-array/
"""
Given a non-empty array of non-negative integers nums, the degree of this 
array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) 
subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
"""

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:    return 0
        n = len(nums)
        l, r, c = {}, {}, {}
        for i, v in enumerate(nums):
            c[v] = c.get(v, 0) + 1
            l[v] = min(l.get(v, n), i)
            r[v] = max(r.get(v, 0), i)
        xx = sorted(list(c.items()), key=lambda x:(x[1]))
        ans = n
        for i in range(len(xx)-1, -1, -1):
            v, freq = xx[i]
            ans = min(ans, r[v] - l[v] + 1)
            if i-1 >= 0 and xx[i-1][1] < freq:
                break
        return ans
                