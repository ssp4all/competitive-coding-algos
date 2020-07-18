https://leetcode.com/problems/dungeon-game/

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
         