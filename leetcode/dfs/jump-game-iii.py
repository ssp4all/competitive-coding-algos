https://leetcode.com/problems/jump-game-iii/

"""
Given an array of non-negative integers arr, you are initially positioned 
at start index of the array. When you are at index i, you can jump to i + arr[i] 
or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if not arr: return 0 
        n = len(arr)
        seen = set()
        @functools.lru_cache(None)
        def helper(index):
            if not (0 <= index < n) or index in seen:    return 0
            seen.add(index)
            if arr[index] == 0: return 1
            return helper(index + arr[index]) or helper(index - arr[index])
        
        return helper(start)