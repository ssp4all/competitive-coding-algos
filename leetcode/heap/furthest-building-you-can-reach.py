https://leetcode.com/problems/furthest-building-you-can-reach/


"""

You are given an integer array heights representing the heights of buildings, 
some bricks, and some ladders.

You start your journey from building 0 and move to the next building by 
possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next 
building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, 
you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the 
given ladders and bricks optimally.
"""
Time O(NlogK)
Space O(K)
class Solution:
    def furthestBuilding(self, A: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        for i in range(len(A) - 1):
            d = A[i + 1] - A[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(A) - 1


#TLE
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        ans = 0
        n = len(heights)
        
        def helper(idx, B, L): 
            nonlocal ans
            ans = max(ans, idx)
            
            if idx >= n - 1:
                return 
            
            diff = heights[idx + 1] - heights[idx]
            
            if diff > 0 and (B <= 0 and L <= 0):
                return 
            
            if diff <= 0:
                helper(idx + 1, B, L)
            else:
                if diff <= B:
                    helper(idx + 1, B - diff, L)
                    if L > 0:
                        helper(idx + 1, B, L - 1)
        
                elif L > 0:
                    helper(idx + 1, B, L - 1)
        
        helper(0, bricks, ladders)
        return ans
            