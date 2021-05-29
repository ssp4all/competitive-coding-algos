https://leetcode.com/problems/n-queens/

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard
 such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' 
placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

"""

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