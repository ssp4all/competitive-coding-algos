https://leetcode.com/problems/battleships-in-a-board



class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board: return 0
        row = len(board)
        col = len(board[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == '.':  continue
                if i>0  and board[i-1][j] == 'X':
                    continue
                if j>0  and board[i][j-1] == 'X':
                    continue
                ans += 1
        return ans

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board: return 0
        row = len(board)
        col = len(board[0])
        ans = 0
        
        def check(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'X':  return 
            board[i][j] = "@"
            check(i, j+1) 
            check(i, j-1) 
            check(i+1, j) 
            check(i-1, j)
        
        ans = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == "X":
                    check(i, j)    
                    ans += 1
        return ans