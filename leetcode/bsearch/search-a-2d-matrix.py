https://leetcode.com/problems/search-a-2d-matrix/


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        # return (any(target in row for row in matrix))
        
        j = -1
        n = len(matrix[0])
        for row in matrix:
            while j + n >= 0 and row[j] > target:
                j -= 1
            if j + n >=0 and row[j] == target:
                return True
        return False
        
 # TC:O(M*lgN), SC:O(1)       
#         for row in matrix:
#             x = bisect_left(row, target)
#             # print(x)
#             if x >= len(row):   continue
#             return target == row[x]
        
#         return False

"""
Upsolving 

- Idea isto start from rightmost col and first row 
- then it wil be binary search tree
- if tar < val
    dec col
  else
    inc row

"""
# TC:O(M + N), SC:O(1)
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