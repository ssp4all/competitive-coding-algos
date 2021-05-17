https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

"""
Given an array of positive integers target and an array initial 
of same size with all zeros.

Return the minimum number of operations to form a target array 
from initial if you are allowed to do the following operation:

Choose any subarray from initial and increment each value by one.
The answer is guaranteed to fit within the range of a 32-bit signed integer.
 

Example 1:

Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the
 target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.
"""

# TC:O(N), SC:O(1)
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        prev = 0 
        ans = 0 
        
        for element in target:
            ans += min(0, element - prev) 
            prev = element
        
        return ans