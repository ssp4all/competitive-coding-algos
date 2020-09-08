https://leetcode.com/problems/brick-wall/

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