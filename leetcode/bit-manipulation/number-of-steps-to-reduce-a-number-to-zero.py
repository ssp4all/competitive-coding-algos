https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

"""
Given a non-negative integer num, return the number of steps to 
reduce it to zero. If the current number is even, you have to 
divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:

Input: num = 14
Output: 6
"""

# simulation
# TC:O(lgn), SC:O(1)
class Solution:
    def numberOfSteps (self, num: int) -> int:
        
        steps = 0 
        while num > 0:
            if num & 1 == 1:
                num -= 1 
            else:
                num //= 2
            steps += 1
        return steps

#better
# TC:O(lgn), SC:O(1)
class Solution:
    def numberOfSteps (self, num: int) -> int:
        if not num: return 0
        op = 0
        while num:
            op += (2 if num & 1 else 1) #add 2 becoz for odd - there are 2 operations 
            							# and for even there is one
            num >>= 1
        return op - 1			#for the last one, only one operation is enough.