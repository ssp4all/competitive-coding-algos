https://leetcode.com/problems/ugly-number-ii/

"""
264. Ugly Number II
Medium

1854

119

Add to List

Share
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if not n: return 0
        
        dp = [0] * n
        dp[0] = 1
        i2, i3, i5 = [0] * 3
        
        n2, n3, n5 = 2, 3, 5
        for i in range(1, n):
            dp[i] = min(n2, n3, n5)
            
            if dp[i] == n2:
                i2 += 1
                n2 = dp[i2] * 2
            if dp[i] == n3:
                i3 += 1
                n3 = dp[i3] * 3
            if dp[i] == n5:
                i5 += 1
                n5 = dp[i5] * 5
        return dp[-1]