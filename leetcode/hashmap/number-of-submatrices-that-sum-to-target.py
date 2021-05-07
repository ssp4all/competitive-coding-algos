https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

"""
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with 
x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they 
have some coordinate that is different: for example, if x1 != x1'.

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0  
Output: 4

"""


# TC:O(MN^2), SC:O(N)
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        #prefix 
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
            
        print(matrix)
        count = 0
        
        for i in range(n):
            for j in range(i, n):
                counter = collections.defaultdict(int)
                counter[0] = 1 
                sum_ = 0
                for k in range(m):
                    sum_ += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    count += counter[sum_ - target]
                    counter[sum_] += 1
                    print(i, j, k, counter, count)
        
        return count