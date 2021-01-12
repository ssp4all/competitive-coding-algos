https://leetcode.com/problems/stone-game/

"""
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, 
and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, 
so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile 
of stones from either the beginning or the end of the row.  This continues until there are no 
more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
"""

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if not piles:   return 0
        
        n = len(piles)
        
        @functools.lru_cache(None)
        def helper(ip, alex, bob, turn):
            if not ip:  return 1 if alex > bob else 0
            if turn == 0:
                return helper(tuple(list(ip)[1:]), alex + ip[0], bob, 1) or \
                            helper(tuple(list(ip)[:-1]), alex + ip[-1], bob, 1)
            else:
                return helper(tuple(list(ip)[1:]), alex, bob + ip[0], 0) or \
                            helper(tuple(list(ip)[:-1]), alex, bob + ip[-1], 0)
                
        return helper(tuple(piles[1:]), 0 + piles[0], 0, 1) or \
                            helper(tuple(piles[:-1]), 0 + piles[-1], 0, 1)

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return 1
        
        n = len(piles)
        @functools.lru_cache(None)
        def DP(i, j):
            if j > i:   return 0
            turn = (j - i - n) % 2
            if turn == 1:
                return max(piles[i] + DP(i + 1, j), piles[j] + DP(i, j - 1))
            else:
                return min(-piles[i] + DP(i + 1, j), -piles[j] + DP(i, j - 1))
        return DP(0, n - 1) > 0
        