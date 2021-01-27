https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

"""
Given an integer n, return the decimal value of the binary string 
formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

Example 1:

Input: n = 1					
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1.
"""

class Solution:
    #TC:O(N), SC:O(1)
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7 
        sum_ = 0
        shift = 0

        for i in range(1, n + 1):
            #now, check if current number is even or not 
            #as in even numbers only have only one set bit 
            #ie, 2 = 10, 4 = 100 

            single_bit = (i & (i - 1) == 0)

            if single_bit == True:
                shift += 1 #for even number of binary digits increases by one not for odd 
            sum_ <<= shift #make space, dude
            sum_ += i 
            sum_ %= MOD 
        return sum_
    
    """
    #TC: O(NlgN), SC:O(1)
    def concatenatedBinary(self, n: int) -> int:
        
        MOD = 10 ** 9 + 7 
        sum_ = 0
        for i in range(1, n + 1):
            sum_ = ((sum_ << len(bin(i)[2:])) + i) % MOD 
        return sum_
    """