https://leetcode.com/problems/pacific-atlantic-water-flow/

"""
Given an m x n matrix of non-negative integers representing the 
height of each unit cell in a continent, the "Pacific ocean" touches 
the left and top edges of the matrix and the "Atlantic ocean" touches the 
right and bottom edges.

Water can only flow in four directions (up, down, left, or right) 
from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific 
and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] 
(positions with parentheses in above matrix).
"""
from collections import deque
class Solution(object):
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]: return []
        row = len(matrix)
        col = len(matrix[0])
        
        def bfs(reachable_state):
            q = deque(reachable_state)
            while q:
                i, j = q.popleft()
                for (x, y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x+i < row and 0 <= y+j < col and \
                        (x+i, y+j) not in reachable_state and \
                            matrix[x+i][y+j] >= matrix[i][j]:
                        q.append((x+i, y+j))
                        reachable_state.add((x+i, y+j))
            return reachable_state

        pacific = set([(0, i) for i in range(col)] + [(i, 0) for i in range(1, row)])
        atlantic = set([(row-1, i) for i in range(col-1)] + [(i, col-1) for i in range(row)])
        return list( bfs(pacific) & bfs(atlantic))
    