https://leetcode.com/problems/cherry-pickup/

"""
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

 

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
 

Your task is to collect maximum number of cherries possible by following the rules below:

 

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
"""

class Solution(object):
    def cherryPickup(self, grid):
        if not grid or not grid[0]: return 0
        
        def get_path(mat):
            """returns maximum cherry path """
            m, n = len(mat), len(mat[0])
            dp = [[float('-inf')] * n for _ in range(m)]
            dp[0][0] = grid[0][0]
            if grid[0][0] < 0:  return []
            
            for j in range(1, n):
                if grid[0][j] != -1:
                    dp[0][j] = max(0, dp[0][j - 1]) + grid[0][j]
            
            for i in range(1, m):
                if grid[i][0] != -1:
                    dp[i][0] = max(0, dp[i - 1][0]) + grid[i][0]
            
            for i in range(1, m):
                for j in range(1, n):
                    if grid[i][j] != -1:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
            # print(dp)
            if dp[-1][-1] < 0:  return []
            path = [(m - 1, n - 1)]
            i, j = m - 1, n - 1
            while i != 0 or j != 0:
                if j - 1 == -1 or i - 1 > -1 and  dp[i - 1][j] >= dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1  
                path += [(i, j)]
                # print(path)
            return path
            
            
        
        path = get_path(grid)
        if not path:    return 0
        # print(path)
        ans = 0
        for i, j in path:
            ans += grid[i][j]
            grid[i][j] = 0
        
        for i, j in get_path(grid):
            ans += grid[i][j]
        return ans