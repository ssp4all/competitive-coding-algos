https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return -1
        
        def edges(mat):
            count = 0
            for row in mat:
                row = [0] + list(row) + [0]
                for i in range(1, len(row)):
                    count += (row[i-1] != row[i])
            return count
        
        tmat = zip(*grid)
        return edges(tmat) + edges(grid)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return -1
        global ans
        def dfs(u, v):
            global ans
            
            if u >= row or v >= col or u < 0 or v < 0:
                ans += 1
                return
            if grid[u][v] == 0:
                ans += 1
                return
            if grid[u][v] not in [1, 0]:
                return
            grid[u][v] = 2
            dfs(u+1, v)
            dfs(u-1, v)
            dfs(u, v+1)
            dfs(u, v-1)
            
            grid[u][v] = 2
            return
        
        row = len(grid)
        col = len(grid[0])
        
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return ans
        return ans