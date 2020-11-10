https://leetcode.com/problems/flipping-an-image/

"""
Given a binary matrix A, we want to flip the image horizontally, 
then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results 
in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
"""

def flipAndInvertImage(self, A):
    return [[1 ^ i for i in reversed(row)] for row in A]

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A or not A[0]:   return A
        
        row, col = len(A), len(A[0])
        
        for i in range(row):
            for j in range(col):
                A[i][j] = (1 if A[i][j] == 0 else 0)
        
        return [row[::-1] for row in A]