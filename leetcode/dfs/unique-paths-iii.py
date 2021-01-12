https://leetcode.com/problems/unique-paths-iii/

"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square 
to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        seen = set()
        ways = [0]
        neigh = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def within(x, y, seen):
            if 0 <= x < m and 0 <= y < n and (x, y) not in seen and grid[x][y] != -1:
                return 1
            return 0
        
        def dfs(i, j, seen, ways):
            if grid[i][j] == 2 and len(seen) == m * n - 1 - obstacles:
                ways[0] += 1
                return
            seen.add((i, j))
            for a, b in neigh:
                ni, nj = i + a, j + b
                if within(ni, nj, seen):
                    dfs(ni, nj, seen, ways)
            seen.remove((i, j))
    
        st_x, st_y = 0, 0
        obstacles = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    st_x, st_y = i, j
                elif grid[i][j] == -1:
                    obstacles += 1
                    
                    
        dfs(st_x, st_y, seen, ways)
        return ways[0]
        
            
            