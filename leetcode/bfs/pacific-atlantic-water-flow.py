https://leetcode.com/problems/pacific-atlantic-water-flow/

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
    