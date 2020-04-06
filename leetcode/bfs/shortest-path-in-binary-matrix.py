https://leetcode.com/problems/shortest-path-in-binary-matrix/

"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only 
if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally 
(ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  
If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        r, c = len(grid), len(grid[0])
        if grid[0][0] or grid[-1][-1]:  return -1
        
        q = [(0, 0, 1)]
        for i, j, d in q:
            if i == r - 1 and j == c - 1:
                return d
                
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
                
                nx, ny = x + i, y + j
                if (0 <= nx < r and 0 <= ny < c) and not grid[nx][ny]:
                    grid[nx][ny] = 1
                    q.extend([(nx, ny, d + 1)])
        return -1
        
#         op = [[float('inf')]*c for _ in range(r)]
#         op[0][0] = 1
#         for i in range(1, c):
#             if grid[0][i] == 1:
#                 continue
#             op[0][i] = 1 + op[0][i - 1]
            
#         for i in range(1, r):
#             if grid[i][0] == 1:
#                 continue
#             op[i][0] = 1 + op[i - 1][0]
#         # print(op)

#         for i in range(1, r):
#             for j in range(1, c):
#                 if grid[i][j] == 1:
#                     continue
#                 mini = float('inf')
#                 for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
#                     nx, ny = x + i, y + j
#                     if (0 <= nx < r and 0 <= ny < c) and grid[nx][ny] != 1:
#                         mini = min(mini, op[nx][ny])
#                 op[i][j] = mini + 1
        
#         print(op)
                    
#         return op[-1][-1] if op[-1][-1] != float('inf') else -1
 