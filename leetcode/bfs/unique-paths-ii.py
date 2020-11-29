https://leetcode.com/problems/unique-paths-ii/

"""
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

import collections
# TLE 
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:    return 0
        r = len(grid)
        c = len(grid[0])
        if grid[0][0] == 1: return 0
        elif grid[0][0] == 0 and (r - 1 == 0 and c - 1 == 0):   return 1   
        dq = collections.deque([(0, 0)])
        # seen = set()
        cnt = 0
        while dq:
            x, y = dq.popleft()
            for i, j in [(1, 0), (0, 1)]:
                nx, ny = x + i, y + j
                if (nx >= r or ny >= c):
                    continue
                if grid[nx][ny] == 1:
                    continue
                elif nx == r - 1 and ny == c - 1:
                    cnt += 1
                else:
                    dq.append((nx, ny))
        return cnt

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:    return 0
        r = len(grid)
        c = len(grid[0])
        if grid[0][0] == 1: return 0
        elif grid[0][0] == 0 and (r - 1 == 0 and c - 1 == 0):   return 1   
        grid[0][0] = 1
        
        for i in range(1, c):
            grid[0][i] = int(grid[0][i - 1] == 1 and grid[0][i] == 0)
        
        for i in range(1, r):
            grid[i][0] = int(grid[i - 1][0] == 1 and grid[i][0] == 0)
        
        for i in range(1, r):
            for j in range(1, c):
                if grid[i][j] == 1:
                    grid [i][j] = 0
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[r - 1][c - 1]    

# https://leetcode.com/problems/unique-paths/
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

# recursive
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = dict()
        def helper(i, j):
            print(i, j)
            if (i, j) in cache:
                return cache[(i, j)]
            if i == m - 1 and j == n - 1:
                return 1
            if i < m - 1 and j < n - 1:
                return helper(i + 1, j) + helper(i, j + 1)
            
            if i < m - 1:
                return helper(i + 1, j)
            if j < n - 1:
                return helper(i, j + 1)
            cache[(i, j)] = 
            return 0
        return helper(0, 0)