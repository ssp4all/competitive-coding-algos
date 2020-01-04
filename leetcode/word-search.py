https://leetcode.com/problems/word-search

from copy import deepcopy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return 0
        nn = len(word)
        
        def dfs(i, j, t, board):
            if i >= row or j >= col or i < 0 or j < 0 or board[i][j] == "@" or t > nn:
                return 0
            tmp = board[i][j]
            if board[i][j] == word[t]:
                board[i][j] = "@"
                t += 1
            else:
                return 0
            if t == nn: return 1
            res = dfs(i+1, j, t, board) or \
                        dfs(i-1, j, t, board) or \
                            dfs(i, j+1, t, board) or \
                                dfs(i, j-1, t, board)
            board[i][j] = tmp
            return res
            
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                t = 0
                if board[i][j] == word[t]:
                    if dfs(i, j, t, board):
                        return 1
        return 0
        