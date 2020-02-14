https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:  return
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = \
                    matrix[j][i], matrix[i][j]
            
        # matrix[:] = zip(*[*matrix])
        # # for i, row in enumerate(matrix):
        # matrix[:]= (matrix[i][::-1] for i in range(len(matrix[0])))
        