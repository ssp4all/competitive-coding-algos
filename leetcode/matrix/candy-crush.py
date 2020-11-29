https://leetcode.com/problems/candy-crush/

"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, 
different positive integers board[i][j] represent different types 
of candies. A value of board[i][j] = 0 represents that the cell at 
position (i, j) is empty. The given board represents the state of the
 game following the player's move. Now, you need to restore the board 
 to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or 
horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board 
has candies on top of itself, then these candies will drop until they hit 
a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. 
If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board 
is stable), then return the current board.
You need to perform the above rules until the board becomes stable, 
then return the current board.
"""

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows = len(board)
        cols = len(board[0])
        remaining_to_crush = False
        
        # 1st idea is to use a representative element like * for marking the candies that need to be crushed but that will fail for the L case
        # Finding all the similar candies in a row
        for i in range(rows):
            for j in range(cols-2):
                if abs(board[i][j])==abs(board[i][j+1])==abs(board[i][j+2])!=0:
                    board[i][j]=-1*abs(board[i][j])
                    board[i][j+1]=-1*abs(board[i][j])
                    board[i][j+2]=-1*abs(board[i][j])
                    remaining_to_crush = True
        
        # Finding all the similar candies in a col
        for i in range(rows-2):
            for j in range(cols):
                if abs(board[i][j])==abs(board[i+1][j])==abs(board[i+2][j])!=0:
                    board[i][j]=-1*abs(board[i][j])
                    board[i+1][j]=-1*abs(board[i][j])
                    board[i+2][j]=-1*abs(board[i][j])
                    remaining_to_crush = True
        
        # Found all the candies that need to be crushed, now use gravity, so iterate through every col
        
        for j in range(cols):
            zeroes = rows-1
            for i in range(rows-1,-1,-1):
                if board[i][j]>0:
                    board[zeroes][j] = board[i][j]
                    zeroes-=1
            
            for x in range(zeroes,-1,-1):
                board[x][j]=0
            
        
        return self.candyCrush(board) if remaining_to_crush else board
            
            
        