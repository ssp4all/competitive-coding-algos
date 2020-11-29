https://leetcode.com/problems/longest-mountain-in-array/

"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
"""

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:   return 0
        n = len(A)
        
        maxi = 0
        base = 0
        while base < n:
            j = base
            if j + 1 < n and A[j + 1] > A[j]:
                while j + 1 < n and A[j + 1] > A[j]:
                    j += 1
                if j + 1 < n and A[j + 1] < A[j]:
                    while j + 1 < n and A[j + 1] < A[j]:
                        j += 1
                    maxi = max(maxi, j - base + 1)
            base = max(j, base + 1)
        return maxi

TLE
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:   return 0
        n = len(A)
        
        maxi = 0
        for i in range(n):
            size = 1
            j = i
            inc, dec = 0, 0
            while j + 1 < n and A[j + 1] > A[j]:
                inc = 1
                size += 1
                j += 1
            
            while j + 1 < n and A[j + 1] < A[j]:
                dec = 1
                j += 1
                size += 1
            if inc and dec:
                maxi = max(maxi, size)
        
        return maxi if maxi > 1 else 0