https://leetcode.com/problems/corporate-flight-bookings/

"""
There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

 

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
"""

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        if not bookings or not bookings:    return []
        count = [0] * (n + 1)
        
        for i, j, k in bookings:
            count[i - 1] += k
            count[j] -= k
        
        for i in range(1, n):
            count[i] += count[i - 1]
            
        return count[:-1]