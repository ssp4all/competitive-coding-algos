https://leetcode.com/problems/divide-two-integers

"""
Given two integers dividend and divisor, divide two integers without using multiplication,
 division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the
 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that 
 your function returns 231 − 1 when the division result overflows.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX =  2 ** 31 - 1
        if dividend == -INT_MAX - 1 and divisor == -1:   return INT_MAX
        
        ans = abs(dividend)  // abs(divisor)
        
        def is_negative():
            return -1 if (dividend < 0 or divisor < 0) \
                                and not (dividend < 0 and divisor < 0) else 1
   
        ans =  ans * is_negative()

        return ans

# upsolving 
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX =  2 ** 31 - 1
        if dividend == -INT_MAX - 1 and divisor == -1:   return INT_MAX
        
        pos_divisor = abs(divisor)
        
        def division(tempDivident, tempDivisor):
            quotient = 1
            if tempDivident == tempDivisor:
                return 1
            elif tempDivident < tempDivisor:
                return 0 

            while (tempDivisor << 1) <= tempDivident:
                quotient <<= 1
                tempDivisor <<= 1 

            quotient += division(tempDivident - tempDivisor, pos_divisor)
            return quotient

        def is_negative():
            return -1 if (dividend < 0 or divisor < 0) \
                                and not (dividend < 0 and divisor < 0) else 1
   
        quotient = division(abs(dividend), abs(divisor))
        
        return quotient * is_negative()