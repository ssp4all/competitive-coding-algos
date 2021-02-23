https://leetcode.com/problems/rotting-oranges/

"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent 
to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse 
until no cell has a fresh orange. If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        global ans
        ans = 0
        row = len(grid)
        col = len(grid[0])
        
        que = deque([])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    que.append((i, j, 0))
        
        def neigh(x, y):
            for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)): 
                if 0 <= a < row and 0 <= b < col:   
                    yield a, b
        
        d = 0
        while que:
            x, y, d = que.popleft()
            for a, b in neigh(x, y):
                if grid[a][b] == 1:
                    grid[a][b] = 2
                    que.append((a, b, d+1))
        if any(1 in row for row in grid):
            return -1
        return d