https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: 
left, right, up or down. You may NOT move diagonally or 
move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        r, c = len(matrix), len(matrix[0])
        cache = dict()
        ans = 0
        # seen = set()
        def dfs(a, b, prev):

            if not ( 0 <= a < r and 0 <= b < c) or (matrix[a][b] <= prev):
                return 0
            # print(cache, a, b, matrix[a][b], prev)

            if (a, b) in cache: 
                return cache[(a, b)]
            # seen.add((a, b))
            temp = matrix[a][b]
            x = 1 + max( [dfs(a+i, b+j, temp) for i, j in [(1, 0), (0, 1), (0, -1), (-1, 0)]])
            cache[(a, b)] = x
            return x
        
        for i in range(r):
            for j in range(c):
                # seen.clear()
                x = dfs(i, j, float('-inf'))
                ans = max(ans, x)
        return ans