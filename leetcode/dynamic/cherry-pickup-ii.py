https://leetcode.com/problems/cherry-pickup-ii/

"""
Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents the number of cherries that you can collect.


You have two robots that can collect cherries for you, Robot #1 is located at the top-left 
corner (0,0) , and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

Return the maximum number of cherries collection using both robots  by following the rules 
below:

From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).

When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).

When both robots stay on the same cell, only one of them takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in the grid.

Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
"""

# TC:O(M*N*N), SC: O(M*N*N)
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @lru_cache(None)
        def dp(row, col1, col2):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return -inf
            # current cell
            result = 0
            result += grid[row][col1]
            if col1 != col2:
                result += grid[row][col2]
            # transition
            if row != m-1:
                result += max(dp(row+1, new_col1, new_col2)
                              for new_col1 in [col1, col1+1, col1-1]
                              for new_col2 in [col2, col2+1, col2-1])
            return result

        return dp(0, 0, n-1)