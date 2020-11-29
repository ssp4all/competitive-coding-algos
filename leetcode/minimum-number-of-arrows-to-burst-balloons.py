https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/

"""
There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x:x[1])
        # print(points)
        start = points[0][1]
        ans = 1
        n = len(points)
        for i in range(1, n):
            if start >= points[i][0]:
                continue
            ans += 1
            start = points[i][1]
        return ans

#############
# on my own
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:  return 0
        
        count = 1
        
        points.sort(key=lambda x:x[1])
        
        pa, pb = points[0]
        
        for st, end in points[1:]:
            if not(pa <= st <= pb or st <= pa <= end):
                count += 1
                pa, pb = st, end
        return count