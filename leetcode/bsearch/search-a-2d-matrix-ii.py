https://leetcode.com/problems/search-a-2d-matrix-ii/

from functools import reduce
from bisect import *

class Solution:
    def searchMatrix(self, matrix, target):
    
        if not matrix or not matrix[0]:  return False
        
        # return any(target in row for row in matrix)

        for i, row in enumerate(matrix):
            x = bisect_left(row, target)
            if x >= len(row):
                continue
            if target == row[x]:
                return True
        return False

class Solution:
    def searchMatrix(self, matrix, target):
        
        if not matrix or not matrix[0]:  return False
        j = -1
        for i, row in enumerate(matrix):
            while j + len(row) >= 0 and row[j] > target:
                j -= 1
            if j + len(row) >= 0 and target == row[j]:
                return True
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return 0 
        
        row = len(matrix)
        col = len(matrix[0])
        
        i = 0 #for row
        j = col - 1 #for col
        
        while j >= 0 and i < row:
            val = matrix[i][j]
            if val == target:
                return 1 
            elif val > target:
                j -= 1
            else:
                i += 1
        return 0