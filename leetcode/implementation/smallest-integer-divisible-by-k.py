https://leetcode.com/problems/smallest-integer-divisible-by-k

"""
Given a positive integer K, you need to find the length of the 

smallest positive integer N such that N is divisible by K, and N 
only contains the digit 1.

Return the length of N. If there is no such N, return -1.

Note: N may not fit in a 64-bit signed integer.

Example 1:

Input: K = 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.

"""

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:    return -1
        
        start = 0
        for i in range(K + 1):
            start = (start * 10 + 1) % K
            if not start:   return i + 1
        return -1

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 1:  return 1
        st = 1
        
        for _ in range(K + 1):
            st = st * 10 + 1
            if st % K == 0:
                return len(str(st))
        return -1
        