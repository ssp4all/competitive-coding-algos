https://leetcode.com/problems/dungeon-game/

"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner 
of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant 
knight (K) was initially positioned 
in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
 If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) 
upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that 
increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only 
rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to 
rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 
if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)  -3  3
-5  -10 1
10  30  -5 (P)

"""
from functools import lru_cache
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon and not dungeon[0]: return 0
        row, col = len(dungeon), len(dungeon[0])
        @lru_cache(None)
        def helper(i, j):
            if not(0 <= i < row and 0 <= j < col):  return float('inf')
            if (i, j) == (row - 1, col - 1):    return max(1, 1 - dungeon[row - 1][col - 1])
            x = max(min(helper(i + 1, j), helper(i, j + 1)) - dungeon[i][j], 1)
            return x
        return helper(0, 0)
            

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon and not dungeon[0]: return 0
        
        row, col = len(dungeon), len(dungeon[0])
        
        dungeon[-1][-1] = max(1, 1 - dungeon[-1][-1])
        
        for i in range(col - 2, -1, -1):
            dungeon[row - 1][i] = max(1, dungeon[row -1 ][i + 1] - dungeon[row -1 ][i])
            
        for i in range(row - 2, -1, -1):
            dungeon[i][col - 1] = max(1, dungeon[i + 1][col - 1] - dungeon[i][col - 1])

        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dungeon[i][j] = max(1, min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j])
          
        return dungeon[0][0]
         