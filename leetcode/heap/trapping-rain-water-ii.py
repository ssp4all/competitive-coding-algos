https://leetcode.com/problems/trapping-rain-water-ii/

"""
Given an m x n integer matrix heightMap representing the 
height of each unit cell in a 2D elevation map, return the 
volume of water it can trap after raining.
"""

#TC:O(M*N lg(M*N)), SC:O(M*N)
class Solution:
    def trapRainWater(self, matrix: List[List[int]]) -> int:
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)] #directions 
        
        heap = []
        rows, cols = len(matrix), len(matrix[0])
        seen = [[0] * cols for _ in range(rows)]
        if not matrix or not matrix[0]: return 0
        
        for i in range(rows): #insert first & last col
            heappush(heap, (matrix[i][0], i, 0))
            heappush(heap, (matrix[i][cols - 1], i, cols - 1))
            seen[i][0] = 1
            seen[i][cols - 1] = 1
            
        for j in range(cols): # insert first & last row
            heappush(heap, (matrix[0][j], 0, j))
            heappush(heap, (matrix[rows - 1][j], rows - 1, j))
            seen[0][j] = 1 
            seen[rows - 1][j] = 1
        
        def within(i, j):
            return 0 <= i < rows and \
                        0 <= j < cols  \
                            and seen[i][j] == 0
        water = 0
        while heap:
            val, i, j = heappop(heap)
            for x, y in dirs:
                ni, nj = i + x, j + y
                if not within(ni, nj):  continue 
                water += max(0, val - matrix[ni][nj]) 
                heappush(heap, (max(val, matrix[ni][nj]), ni, nj))
                seen[ni][nj] = 1 
        return water