https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

"""
Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). 
In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner 
(0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at 
most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. 
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]: return -1
        
        r, c = len(grid), len(grid[0])
        seen = set()
        
        q = collections.deque([(0, 0, k, 0)])
        if k > (r + c - 2):
            return r + c - 2
        while q:
            i, j, e, s = q.popleft()
            
            
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ni, nj = x + i, y + j
                if (0 <= ni < r and 0 <= nj < c):
                    if grid[ni][nj] == 1 and e > 0 and\
                                (ni, nj, e - 1) not in seen: 
                        q.append((ni, nj, e - 1, s + 1))
                        seen.add((ni, nj, e - 1))
                    if grid[ni][nj] == 0 and (ni, nj, e) not in seen:
                        if ni == r - 1 and nj == c - 1:
                            return s + 1
                        q.append((ni, nj, e, s + 1))
                        seen.add((ni, nj, e))

        return -1


from heapq import *
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]: return -1
        r, c = len(grid), len(grid[0])
        ans = []
        
        def dfs(m, n, s, obj):
            nonlocal ans
            if m == r - 1 and n == c - 1:
                heappush(ans, (obj, s))
                return
            if grid[m][n] == 1:
                obj += 1
            s += 1
            temp = grid[m][n]
            grid[m][n] = "@"
            for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nm, nn = m + i, n + j
                if (0 <= nm < r and 0 <= nn < c) and grid[nm][nn] != "@":
                    dfs(nm, nn, s, obj)
            grid[m][n] = temp
            if grid[m][n] == 1:
                obj -= 1
            s -= 1
            
        dfs(0, 0, 0, 0)
        print(ans)
        if ans[0][0] > k:
            return -1
        return ans[0][1]
        
            