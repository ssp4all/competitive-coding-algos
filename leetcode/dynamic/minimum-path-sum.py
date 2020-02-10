https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid  or not grid[0]:    return 0
        r = len(grid)
        c = len(grid[0])
        
        for i in range(1, c):
            grid[0][i] += grid[0][i - 1]
        
        for i in range(1, r):
            grid[i][0] += grid[i- 1][0]
        
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid  or not grid[0]:    return 0
        global ans
        row = len(grid)
        col = len(grid[0])
        seen = set()
        ans, mini = float('inf'), 0
        def bt(x, y, psum):
            global ans
            if (x, y) == (row - 1, col - 1):
                psum += grid[x][y]
                ans = min(ans, psum)
            else:
                psum += grid[x][y]
                seen.add((x, y))
                for (a, b) in [(1, 0), (0, 1)]:
                    nx, ny = x + a, y + b
                    if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in seen:
                        bt(nx, ny, psum)
            if (x, y) in seen:
                seen.remove((x, y))
            
        bt(0, 0, 0)
        return ans
            