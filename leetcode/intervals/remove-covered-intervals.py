https://leetcode.com/problems/remove-covered-intervals/

"""
Given a list of intervals, remove all intervals that are covered by 
another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:   return 0
        intervals.sort(key=lambda x:x[1])
        res = [intervals[0]]    
        n = len(intervals)
        for i in range(1, n):
            c, d = intervals[i]  
            while res and (c <= res[-1][0] and res[-1][1] <= d or \
                res[-1][0] <= c and d <= res[-1][1]):                
                res.pop()
            res += [[c, d]]
        return len(res)