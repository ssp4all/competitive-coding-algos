
https://leetcode.com/problems/car-pooling/

"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about 
the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  
The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
"""

from heapq import *

# TC:O(NlgN), SC:O(N)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        if n <= 0:  return 0
        trips.sort(key=lambda x:x[1])
        p, st, end = trips[0]
        
        destinations = [(end, p)]
        cur = p
        for trip in trips[1:]:
            passen, n_st, n_end = trip
            while destinations and destinations[0][0] <= n_st:
                des, p = heappop(destinations)
                cur -= p
                
            heappush(destinations, (n_end, passen))
            cur += passen
            if cur > capacity:  return 0
            
        return 1

"""
[[2,1,5],[3,3,7]]
4
[[3,2,8],[4,4,6],[10,8,9]]
11
[[3,2,7],[3,7,9],[8,3,9]]
11
"""