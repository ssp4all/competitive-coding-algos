def min_lec(lec):
	n = len(lec)
	prefix = [0]*20
	for i in range(n):
		prefix[lec[i][0]] += 1
		prefix[lec[i][1] + 1] -= 1
	print(prefix)
	ans = prefix[0]

	for i in range(1, 20):
		prefix[i] += prefix[i-1]
		ans = max(ans, prefix[i])
	print(ans)

lec = [[ 0, 5 ], [ 1, 2 ], [ 1, 10 ]]
min_lec(lec)


# https://leetcode.com/problems/meeting-rooms-ii/

"""
Given an array of meeting time intervals consisting of start 
and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

class Solution:
    def minMeetingRooms(self, inter: List[List[int]]) -> int:
        if not inter or not inter[0]: return 0
        
        inter.sort(key = lambda x:(x[1]))
        end = inter[-1][1]
        dp = [0] * (end + 1)
        n = len(inter)
        for i in range(n):
            dp[inter[i][0]] += 1
            dp[inter[i][1]] -= 1
        ans, maxx = dp[0], float('-inf')
        
        for i in range(end - 1):
            dp[i+1] += dp[i]
            ans = max(ans, dp[i+1])
        return ans

# heap solution
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, inter: List[List[int]]) -> int:
        if not inter or not inter[0]: return 0
        
        inter.sort(key = lambda x:(x[1]))
        heap = []
        heappush(heap, inter[0][1])
        n = len(inter)
        
        for i in range(1, n):
            if inter[i][0] >= heap[0]:
                heappop(heap)
            heappush(heap, inter[i][0])
        return len(heap)