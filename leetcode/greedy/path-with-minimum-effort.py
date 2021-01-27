https://leetcode.com/problems/path-with-minimum-effort/


"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size 
rows x columns, where heights[row][col] represents the height of cell (row, col). You are 
situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, 
(rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you 
wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive 
cells of the route.

Return the minimum effort required to travel from the top-left cell to the 
bottom-right cell.

[[1,2,3],[3,8,4],[5,3,5]]
OP: 1 
"""

#TC:ElgV => M*N*lg(M*N), SC:O(M*N)
class Solution:
    
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        
        dist = [[float('inf')] * n for _ in range(m)]
        
        def within(a, b):
            return 0 <= a < m and 0 <= b < n
        
        nei = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        minHeap = []
        minHeap.append((0, 0, 0))  # distance, row, col
        
        while minHeap:
            d, r, c = heappop(minHeap)
            if d > dist[r][c]: continue
            if r == m - 1 and c == n - 1:
                return d  # Reach to bottom right
            for a, b in nei:
                nr, nc = r + a, c + b
                if within(nr, nc):
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))
        return -1
