https://leetcode.com/problems/spiral-matrix-ii/

"""
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:   return [[]]
        
        matrix = [[None for _ in range(n)] for _ in range(n)]
        
        rowstart, rowend = 0, n - 1
        colstart, colend = 0, n - 1
        num = 1 
        
        while rowstart <= rowend and colstart <= colend:
            
            for i in range(colstart, colend + 1):
                matrix[rowstart][i] = num 
                num += 1
            rowstart += 1
            
            for i in range(rowstart, rowend + 1):
                matrix[i][colend] = num
                num += 1
            colend -= 1
            
            for i in range(colend, colstart - 1, -1):
                matrix[rowend][i] = num 
                num += 1
            rowend -= 1
            
            for i in range(rowend, rowstart - 1, -1):
                matrix[i][colstart] = num
                num += 1
            colstart += 1
        
        return matrix