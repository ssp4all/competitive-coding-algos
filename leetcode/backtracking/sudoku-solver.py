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
        