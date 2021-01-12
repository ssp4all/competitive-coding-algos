https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        n1 = len(grid)
        n2 = len(grid[0])
        global ans, size
        def dfs(i, j):
            global ans, size
            if i >= n1 or i<0 or j<0 or j>=n2 or grid[i][j] != 1:
                return 
            grid[i][j] = "@"
            size += 1
            ans = max(ans, size)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i-1, j)
            
        ans = 0
        for i in range(n1):
            for j in range(n2):
                if grid[i][j] == 1:
                    size = 0
                    dfs(i, j)
        return ans

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        n1 = len(grid)
        n2 = len(grid[0])
        visited = set()
        def dfs(u, v):
            if not (0<=u<n1 and 0<=v<n2 and grid[u][v] and (u, v) not in visited):
                return 0
            visited.add((u, v))
            return (1 + dfs(u+1, v) + 
                        dfs(u, v+1) +
                        dfs(u, v-1) +
                        dfs(u-1, v))
        
        return max(dfs(u, v) 
                   for u in range(n1)
                    for v in range(n2)  )
        