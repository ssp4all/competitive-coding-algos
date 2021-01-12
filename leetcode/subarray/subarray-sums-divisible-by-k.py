https://leetcode.com/problems/subarray-sums-divisible-by-k/

"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays
 that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)
        if n == 0:  return 0
        
        count = 0
        sum_ = 0
        lookup = {0:1}
        
        for i in range(n):
            sum_ += A[i]
            sum_ %= K
            # if sum_ < 0:    sum_ += K
            count += lookup.get(sum_, 0)
            lookup[sum_] = lookup.get(sum_, 0) + 1
        return count

Brute force
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)
        if n == 0:  return 0
        count = 0
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += A[j]
                if sum_ % K == 0:   count += 1
        return count