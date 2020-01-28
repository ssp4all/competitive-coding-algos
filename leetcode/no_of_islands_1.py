https://leetcode.com/problems/number-of-islands/submissions/

- Number of distrinct islands and also count too

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        row = len(grid)
        col = len(grid)
        seen = set()
        
        def explore(r, c, di = 0):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.append(di)
                explore(r+1, c, 1)
                explore(r-1, c, 2)
                explore(r, c+1, 3)
                explore(r, c-1, 4)
                shape.append(0)
        ans = 0
        shapes = set()
        for i in range(row):
            for j in range(col):
                shape = []
                if (i, j) not in seen and grid[i][j] == 1:
                    explore(i, j, 0)
                    ans += 1
                    if shape:
                        shapes.add(tuple(shape))
                        # print(shapes)
        # print(ans)
        return len(shapes)

class Solution:
    def numIslands(self, board: List[List[str]]) -> int:
        if not board: return 0
        row = len(board)
        col = len(board[0])
        ans = 0
        seen = set()
        def dfs(u, v):
            seen.add((u,v))
            
            if (u + 1 < row) and ((u+1, v) not in seen) and (board[u+1][v] == "1"):
                dfs(u+1, v)
            if u - 1 >= 0 and (u-1, v) not in seen and board[u-1][v] == "1":
                dfs(u-1, v)
            if v + 1 < col and (u, v+1) not in seen and board[u][v+1] == "1":
                dfs(u, v+1)
            if v - 1 >= 0 and (u, v-1) not in seen and board[u][v-1] == "1":
                dfs(u, v-1)
            
        for i in range(row):
            for j in range(col):
                if (i, j) not in seen and board[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans

Recursive dfs

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

BFS  iterative

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        ans = 0
        row = len(grid)
        col = len(grid[0])
        que = deque()
        seen = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in seen:
                    ans += 1
                    que.append((i, j))
                    while que:
                        x, y = que.popleft()
                        
                        if 0 <= x < row and 0 <= y < col and grid[x][y] == "1" \
                                and (x, y) not in seen:
                            seen.add((x, y))    
                            que.extend([(x, y+1), (x, y-1), (x+1, y), (x-1, y)])
        return ans
                            
                        