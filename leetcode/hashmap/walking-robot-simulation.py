https://leetcode.com/problems/walking-robot-simulation

"""
A robot on an infinite grid starts at point (0, 0) and faces north.  
The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous 
grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        dir = {'s': (0, -1), 'w': (-1, 0), 'n': (0, 1), 'e': (1, 0)}
        x, y = 0, 0
        cur = 'n'
        ans = float('-inf')
        for c in commands:
            if c == -2: #left
                if cur == 'n': cur = 'w'
                elif cur == 'w': cur = 's'
                elif cur == 's': cur = 'e'
                elif cur == 'e': cur = 'n'
                
                    
            elif c == -1: #right
                if cur == 'n': cur = 'e'
                elif cur == 'w': cur = 'n'
                elif cur == 's': cur = 'w'
                elif cur == 'e': cur = 's'
                
            else:
                while c > 0 and \
                        (x + dir[cur][0], y + dir[cur][1]) not in obs:
                    x, y = x + dir[cur][0], y + dir[cur][1]
                    c -= 1
            ans = max(ans, (x*x + y*y))
        return ans