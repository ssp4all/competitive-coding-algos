https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

"""
A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
"""

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if not weights: return 0
        n = len(weights)
        tot = 0
        mx = 0
        for w in weights:
            tot += w
            mx = max(mx, w)
        
        def feasible(cur):
            d, tot = 1, 0
            for w in weights:
                tot += w
                if tot > cur:
                    tot = w
                    d += 1
                    if d > D:
                        return 0
            return 1
        l, r = mx, tot
        while l < r:
            m = l + (r - l) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1
        return l