https://leetcode.com/problems/number-of-closed-islands/
"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 
4-directionally connected group of 0s and a closed island is an island totally 
(all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
"""
"""
Idea:
- mark all lands on edges to water 
- Find islands using dfs
"""
# TC:O(M*N), SC:O(1) except recursion space which is O(M*N)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0 
        
        row, col = len(grid), len(grid[0])
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def within(x:int, y:int)->bool: #check if in the grid
            return (0 <= x < row and 0 <= y < col)
        
        def dfs(i:int, j:int)->None:
            if not within(i, j) or grid[i][j] == 1:    return 
            grid[i][j] = 1
            for x, y in directions:
                ni, nj = i + x, j + y
                dfs(ni, nj)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 and (i in [0, row - 1] or j in [0, col - 1]):
                    dfs(i, j)
        
        count = 0
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        return count
                    