https://leetcode.com/problems/surrounded-regions/


"""
Given an m x n matrix board containing 'X' and 'O', 
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's 
into 'X's in that surrounded region.


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return 
        row = len(board)
        col = len(board[0])
        
        que = []
        for k in range(max(row, col)):
            for (i, j) in [(0, k), (k, 0), (row-1, k), (k, col-1)]:
                que.append((i, j))
        while que:
            (i, j) = que.pop()
            if 0<= i < row and 0<= j < col and board[i][j] == "O":
                board[i][j] = "@"
                que += ((i+1, j), (i-1, j), (i, j-1), (i, j+1))
        
        board[:] = [["XO"[board[i][j] == "@"] for j in range(col)]for i in range(row)]
        