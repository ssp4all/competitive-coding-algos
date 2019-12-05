# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/
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