https://leetcode.com/problems/find-right-interval/

import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if not intervals:   return []
        n = len(intervals)
        
        
        if n == 1:  return [-1]
        op = []
        sorted_arr = sorted([(val[0], ind) for ind, val in enumerate(intervals)])
        
        for interval in intervals:
            a, b = interval
            val = bisect.bisect_left(sorted_arr, (b,))
            if val == n:
                op += [-1]
            else:
                op += [sorted_arr[val][1]]
        return op
        
        # for i in range(n):
        #     a = intervals[i][1]
        #     mini = float('inf')
        #     for j in range(n):
        #         if i == j:  continue
        #         b = intervals[j][0]
        #         if b >= a and b < mini:
        #             op[i] = j
        #             mini = b
        # return op