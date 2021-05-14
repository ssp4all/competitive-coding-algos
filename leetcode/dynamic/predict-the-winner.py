https://leetcode.com/problems/predict-the-winner/

"""
You are given an integer array nums. Two players are 
playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. 
Both players start the game with a score of 0. At each turn, 
the player takes one of the numbers from either end of the 
array (i.e., nums[0] or nums[nums.length - 1]) which 
reduces the size of the array by 1. The player adds 
the chosen number to their score. The game ends when 
there are no more elements in the array.

Return true if Player 1 can win the game. If the 
scores of both players are equal, then player 1 is 
still the winner, and you should also return true. 
You may assume that both players are playing optimally.


Example 1:

Input: nums = [1,5,2]
Output: false 
"""


#TC:O(N^2),  SC:O(N^2)
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if not nums:    return 1 
        n = len(nums)
        
        @functools.lru_cache(None)
        def helper(l, r, turn):
            if l == r:   return nums[l] * turn 
            p1 = turn * nums[l] + helper(l + 1, r, -turn)
            p2 = turn * nums[r] + helper(l, r - 1, -turn)
            return turn * max(turn * p1, turn * p2)
        
        return helper(0, n - 1, 1) >= 0