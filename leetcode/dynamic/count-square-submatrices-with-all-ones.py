https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        r, c = len(matrix), len(matrix[0])

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1

        return sum(map(sum, matrix))
