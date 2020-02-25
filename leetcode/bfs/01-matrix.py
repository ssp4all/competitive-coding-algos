https://leetcode.com/problems/01-matrix/

from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        row, col = len(matrix), len(matrix[0])
        que = deque([])
        
        # op = [[0 for _ in range(col)] for _ in range(row)]
        for i, r in enumerate(matrix):
            for j, val in enumerate(r):
                if not val:
                    que.append((i, j))#all zeroes
                else:
                    matrix[i][j] = float('inf')
                    
        while que:
            (i, j) = que.popleft()
            
            for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i+a, j+b
                if not(0 <= ni < row and 0 <= nj < col) or \
                        (matrix[ni][nj] <= matrix[i][j] + 1):
                    continue
                matrix[ni][nj] = matrix[i][j] + 1
                que.append((ni, nj))
        return matrix
                    
                    
                    
                    
                    
                    