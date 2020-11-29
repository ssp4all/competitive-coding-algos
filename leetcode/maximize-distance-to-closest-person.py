https://leetcode.com/problems/maximize-distance-to-closest-person/

"""
You are given an array representing a row of seats where seats[i] = 1 represents 
a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if not seats:   return 0
        # seats += [1]
        n = len(seats)
        
        last = -1
        maxi = float('-inf')
        
        for i in range(n):
            if seats[i] == 1:
                maxi = max(maxi, i - last)
                last = i
        first = seats.index(1) #find first person
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                last = i        #find last person index
                break
            
        return max(maxi // 2, first, n - 1 - last) # find max of inbetween, first and last


def maxDistToClosest(self, seats):
        res, last, n = 0, -1, len(seats)
        for i in range(n):
            if seats[i]:
                res = max(res, i if last < 0 else (i - last) / 2)
                last = i
        return max(res, n - last - 1)