https://leetcode.com/problems/brick-wall/

"""
There is a brick wall in front of you. The wall is rectangular and 
has several rows of bricks. The bricks have the same height but different width. 
You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers 
representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered 
as crossed. You need to find out how to draw the line to cross the least bricks 
and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, 
in which case the line will obviously cross no bricks.

 

Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2

"""


import collections

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        if n <= 0:  return 0
        
        tot_cuts = 0
        freq = collections.defaultdict(int)
        for i in range(n):
            tot_bricks = len(wall[i])
            if tot_bricks == 1: continue
            freq[wall[i][0]] += 1
            for j in range(1, tot_bricks - 1):
                wall[i][j] += wall[i][j - 1]
                freq[wall[i][j]] += 1

        return n - max(freq.values(), default=0)


# TC:O(N), SC:O(N)
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall:    return 0 
        
        total = 0 
        freq = collections.defaultdict(int)        
        for row in wall:
            sum_ = 0 
            for val in row[:-1]:
                sum_ += val 
                freq[sum_] += 1 
                total = max(total, freq[sum_])
            
        return len(wall) - total