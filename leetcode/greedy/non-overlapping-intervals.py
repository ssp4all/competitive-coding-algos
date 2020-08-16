https://leetcode.com/problems/non-overlapping-intervals/
"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1:   return 0
        intervals.sort(key=lambda x:(x[1]))
        
        prevA, prevB = intervals[0]
        
        ans = 0
        l, r = 1, n
        while l < r:
            a, b = intervals[l]
            if a == prevA or (a < prevB):
                ans += 1
            else:
                prevA, prevB = a, b
            l += 1
        return ans
            