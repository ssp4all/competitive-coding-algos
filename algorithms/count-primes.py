https://leetcode.com/problems/count-primes/

""" 
Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
"""

# TC:O(root of N * lg * lg(N)), SC:O(N)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:   return 0
        
        arr = [1] * n  #mark all numbers as prime 
        arr[0] = arr[1] = 0
        i = 2 
        while i * i < n:
            j = i * i
            while j < n:
                arr[j] = 0 
                j += i             
            i += 1
        
        return sum(arr)