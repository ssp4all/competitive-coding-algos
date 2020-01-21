https://leetcode.com/problems/koko-eating-bananas/

from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if not piles: return 0
        n = len(piles)
        l, r = 1, max(piles)
        maxi = r
        def check(eat):
            tot = 0
            for ban in piles:
                div = ceil(ban / eat)
                tot += div
                if tot > H:
                    return 0
            return 1
        ans = float('inf')
        while l < r:
            m = (l + r) // 2
            if check(m):
                ans = min(ans, m)
                r = m
            else:
                l = m + 1
        return ans if ans != float('inf') else maxi
                
            