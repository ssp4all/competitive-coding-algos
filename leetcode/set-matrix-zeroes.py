https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        row = len(matrix)
        col = len(matrix[0])
        r, c = set(), set()
        zeroes = set()
        for i in range(row):
            for j in range(col):
                if not matrix[i][j]:
                    r.add(i)
                    c.add(j)
        
        for i in range(row):
            if i in r:
                matrix[i] = [0]*col
                
        if len(r) == row: return
        for j in range(col):
            if j in c:
                for z in range(row):
                    matrix[z][j] = 0
                    