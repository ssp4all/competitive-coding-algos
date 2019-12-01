class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        ans = 0
        n1 = len(grid)
        n2 = len(grid[0])
        for i in range(n1):
            for j in range(n2):
                
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    ans += 1
        return ans
                    
    def dfs(self, u, v, grid):
        n1 = len(grid)
        n2 = len(grid[0])
        if u<0 or v<0 or u>=n1 or v>=n2 or grid[u][v] != "1":
            return
        grid[u][v] = "!"
        self.dfs(u, v+1, grid)
        self.dfs(u, v-1, grid)
        self.dfs(u+1, v, grid)
        self.dfs(u-1, v, grid)