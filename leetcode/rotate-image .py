# https://leetcode.com/problems/rotate-image

# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

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
        