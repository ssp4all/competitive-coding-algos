class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        # self.board = [[float('inf') for _ in range(n)] for _ in range(n)]
        self.row, self.col, self.diag, self.anti = [0]*n, [0]*n, 0, 0        

        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        point = 2*player - 3
        self.row[row] += point
        self.col[col] += point
        if row == col:
            self.diag += point
        if row + col == self.n-1:
            self.anti += point
        if self.n in [self.row, self.col, self.diag, self.anti]: return 2
        if self.n*-1 in [self.row, self.col, self.diag, self.anti]: return 1
        return 0
        
        
        
        
#         if player == 1:
#             self.board[row][col] = 0
#         else:
#             self.board[row][col] = 1
#         return  self.check()
    
#     def check(self):
#         row, col = [0]*self.n, [0]*self.n
#         d1, d2 = 0, 0
#         for i in range(self.n):
#             for j in range(self.n):
#                 if i == j: #first diagonal
#                     d1 += self.board[i][j]
#                 if d1 == 0:
#                     return 1
#                 if d1 == self.n: 
#                     return 2
                
#                 row[i] += self.board[i][j]
#                 col[j] += self.board[i][j]
#                 if any(row) == 0 or any(col) == 0: return 1
#                 if any(row[i]) == self.n or any(col) == self.n: return 2
                
        
#         j = self.n-1
#         i = 0
#         while j>=0 and i<n:
#             d2 += self.board[i][j]
#             j -= 1
#             i += 1
        
#         if d2 == 0: return 1
#         if d2 == 1: return 2
#         return 0
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)