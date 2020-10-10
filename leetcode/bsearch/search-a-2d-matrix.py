https://leetcode.com/problems/search-a-2d-matrix/

# from bisect import bisect_left

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
        
        
#         for row in matrix:
#             x = bisect_left(row, target)
#             # print(x)
#             if x >= len(row):   continue
#             return target == row[x]
        
#         return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        # return (any(target in row for row in matrix))
        
        r = len(matrix)
        c = len(matrix[0])
        
        s, e = 0, r * c - 1
        
        while s <= e:
            m = (s + e) // 2
            midv = matrix[m // c][m % c]
            if midv == target:
                return True
            elif midv > target:
                e = m - 1
            else:
                s = m + 1
        return False