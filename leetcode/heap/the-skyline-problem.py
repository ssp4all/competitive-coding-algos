https://leetcode.com/problems/the-skyline-problem/

"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that
 city when viewed from a distance. Now suppose you are given the locations and height of all 
 the buildings as shown on a cityscape photo (Figure A), write a program to output the 
 skyline formed by these buildings collectively (Figure B).
"""

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:   return []
        n = len(buildings)
        
        heights = []
        for x1, x2, h in buildings:
            heights += [(x1, -h), (x2, h)]
        
        heights.sort()
        
        heap = []
        heapq.heappush(heap, 0)
        prev = 0
        res = []
        
        for x, h in heights:

            if h > 0:
                heap.remove(-h)
            else:
                heapq.heappush(heap, h)
            heapq.heapify(heap)
            cur = -heap[0]    
            if prev != cur:
                res += [[x, cur]]
                prev = cur 
            # print((x, h), heap)
        return res

# TC: O(ElnE), SC: E
class Solution:
    def getSkyline(self, buildings):
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]