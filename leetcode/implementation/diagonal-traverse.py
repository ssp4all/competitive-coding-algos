https://leetcode.com/problems/diagonal-traverse

"""
Given a matrix of M x N elements (M rows, N columns), 
return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

"""

# TC: O(N*M + keys)
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return [] 
        
        row, col = len(matrix), len(matrix[0])
        
        elements = collections.defaultdict(list)
        
        for i in range(row):
            for j in range(col):
                elements[i + j] += [matrix[i][j]]
                
        ans = []
        for k, val in elements.items():
            if k % 2 == 0:
                ans += [*val[::-1]]
            else:
                ans += [*val]
        return ans


# https://leetcode.com/problems/diagonal-traverse-ii/
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return [] 
        
        row, col = len(matrix), len(matrix[0])
        
        elements = collections.defaultdict(list)
        
        for i in range(row):
            for j in range(len(matrix[i])):
                elements[i + j] += [matrix[i][j]]

        ans = []
        for k, val in elements.items():
            ans += [*val[::-1]]

        return ans