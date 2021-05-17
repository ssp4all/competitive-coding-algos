https://leetcode.com/problems/triangle/

"""
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

"""
"""
TC
without memoization: TC: O(2^n), SC:O(rows)
with memoization: TC: O(n*n/2), SC:O(n*n/2 + rows)
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:  return 0 
        n = len(triangle)
        @functools.lru_cache(None)
        def helper(row, index):
            if row == n:
                return 0 
            cost = min(helper(row + 1, index) + triangle[row][index], \
                      helper(row + 1, index + 1) + triangle[row][index + 1] )
            return cost 
        return helper(1, 0) + triangle[0][0]

#TC: O(n*n/2), SC:O(N) > N = no of elements in the matrix
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:    return 0 
        
        idx = 0 
        row = 0
        
        @functools.lru_cache(None)
        def helper(row, idx):
            if row >= len(triangle) or idx >= len(triangle[row]):    return 0 
            
            return min(helper(row + 1, idx), helper(row + 1, idx + 1)) + \
                        triangle[row][idx]         
        return helper(0, 0)

# TC:O(n*n/2), SC:O(1)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:  return 0 
        n = len(triangle)
        
        #dp
        triangle[0] = [float('inf')] + triangle[0] + [float('inf')]
        for i in range(1, n):
            triangle[i] = [float('inf')] + triangle[i] + [float('inf')]
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])