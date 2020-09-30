https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended

"""
Given an array of events where events[i] = [startDayi, endDayi]. 
Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. 
Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.
"""

TLE
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:  return 0
        
        events.sort(key=lambda x:x[1])
        
        seen = set()
        count = 0
        n = len(events)
        for i in range(n):
            st, end = events[i]
            for j in range(st, end + 1):
                if j not in seen:
                    seen.add(j)
                    count += 1
                    break
        return count

from heapq import *
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:  return 0
        
        events.sort()
        final_day = max(end for st, end in events)
        heap = []
        
        event, count, day = 0, 0, 1
        while day <= final_day:
            
            while event < len(events) and events[event][0] <= day:
                heappush(heap, events[event][1])
                event += 1
            while heap and heap[0] < day:
                heappop(heap)
            if heap:
                heappop(heap)
                count += 1
            day += 1
            if day > final_day:
                break
        return count
            
"""
[[1,2],[2,3],[3,4]]
[[1,2],[2,3],[3,4],[1,2]]
[[1,4],[4,4],[2,2],[3,4],[1,1]]
[[1,100000]]
[[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
"""
        