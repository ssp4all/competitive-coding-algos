https://leetcode.com/problems/sort-the-matrix-diagonally

"""
A matrix diagonal is a diagonal line of cells starting from some cell in 
either the topmost row or leftmost column and going in the bottom-right 
direction until reaching the matrix's end. For example, the matrix diagonal 
starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells 
mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in
ascending order and return the resulting matrix.

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
"""

# TC:(N*M*log(min(N, M)))
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # hashmap to keep the diagonals
        h = defaultdict(list)
        
        # fill the hashmap
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                heappush(h[i - j], mat[i][j])

        # build output
        for i in range(n):
            for j in range(m):
                mat[i][j] = heappop(h[i - j])
        
        return mat

# TC:O(DlgE + N^2)
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diags = defaultdict(list)
        
        r, c = len(mat), len(mat[0])
        
        for i in range(r):
            for j in range(c):
                diags[i - j] += [mat[i][j]]
        # print(diags)
        for key in diags:
            diags[key].sort(reverse=1)
            
        
        for i in range(r):
            for j in range(c):
                mat[i][j] = diags[i - j].pop()
        
        return mat