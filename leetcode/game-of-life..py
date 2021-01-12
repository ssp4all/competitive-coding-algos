https://leetcode.com/problems/game-of-life/

Brute force

from copy import deepcopy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return 
        if not board[0]:    return
        row = len(board)
        col = len(board[0])
        
        def check(u, v):
            live = 0
            for x, y in [(u+1, v+1), (u-1, v-1), (u+1, v), \
                            (u-1, v), (u, v+1), (u, v-1), \
                                (u+1, v-1), (u-1, v+1)]:
                if 0 <= x < row and 0 <= y < col:
                    if board[x][y] == 1:
                        live += 1
            if live < 2 or live > 3:
                temp[u][v] = 0
                return
            elif live == 3:
                temp[u][v] = 1
                return
            else:
                pass
        temp = deepcopy(board)
        for i in range(row):
            for j in range(col):
                check(i, j)
            
        for i in range(row):
            for j in range(col):
                board[i][j] = temp[i][j]
                
Little optimal

# from copy import deepcopy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return 
        # if not board[0]:    return
        row = len(board)
        col = len(board[0])
        
        def check(u, v):
            lives = 0
            for (x, y) in [(u+1, v+1), (u-1, v-1), (u+1, v), \
                            (u-1, v), (u, v+1), (u, v-1), \
                                (u+1, v-1), (u-1, v+1)]:
                if 0 <= x < row and 0 <= y < col:
                    if abs(board[x][y]) == 1:
                        lives += 1
                        
            if board[u][v] == 0:
                if lives == 3:
                    board[u][v] = 2
            else:
                if lives < 2 or lives > 3:
                    board[u][v] = -1
        
        for i in range(row):
            for j in range(col):
                check(i, j)
            
        for i in range(row):
            for j in range(col):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
                