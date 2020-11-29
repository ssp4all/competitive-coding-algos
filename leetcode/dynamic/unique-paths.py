https://leetcode.com/problems/unique-paths/

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' 
in the diagram below).

The robot can only move either down or right at any point in time. The robot 
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        r, c = m, n
        grid[0][0] = 1
        for i in range(1, c):
            grid[0][i] = int(grid[0][i - 1] == 1)
        
        for i in range(1, r):
            grid[i][0] = int(grid[i - 1][0] == 1)
        
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[r - 1][c - 1]  