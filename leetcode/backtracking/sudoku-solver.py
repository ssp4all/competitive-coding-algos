https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        n = len(board)
        
        def check(row, col, ch):
            for i in range(9):
                if board[row][i] == ch: return 0 
                if board[i][col] == ch: return 0
                nr, nc = (3 * (row // 3) + (i // 3)), (3 * (col // 3) + i % 3)
                if board[nr][nc] == ch: return 0
            return 1
        
        def helper():
            for i, row in enumerate(board):
                for j, val in enumerate(row):
                    if val != '.':
                        continue
                    for c in [str(i) for i in range(1, 10)]:
                        if check(i, j, c):
                            board[i][j] = c
                            if helper():
                                return 1
                            else:
                                board[i][j] = "."
                    return 0
            return 1
        
        helper()
        return
        
https://leetcode.com/problems/n-queens/

""" 

The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration 
of the n-queens' placement, where 'Q' and '.' both indicate 
a queen and an empty space, respectively.
"""

#TC:O(N!), SC:O(N!)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0:  return [] 
        
        res = [] 
        
        def format_board(board: 'list[list]'):
            return ["".join(row) for row in board]
        
        def backtrack(cols: set, diag: set, anti:set, \
                        row: int, col: int, board: 'list[list]'):
            nonlocal res
            if row == n:
                res += [format_board(board)]
                return 
            
            for col in range(n):
                D = row - col # current diagonal 
                AD = row + col # anti diagonal 
                
                if col in cols or D in diag or AD in anti:
                    continue 
                board[row][col] = 'Q'
                diag.add(D)
                anti.add(AD)
                cols.add(col)
                
                backtrack(cols, diag, anti, row + 1, col + 1, board)
                
                #backtrack 
                diag.remove(D)
                anti.remove(AD)
                cols.remove(col)
                
                #remove queen 
                board[row][col] = '.'
            
        
        board = [['.'] * n for _ in range(n)]
        backtrack(set(), set(), set(), 0, 0, board)
        return res