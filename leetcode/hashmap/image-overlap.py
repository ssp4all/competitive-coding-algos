https://leetcode.com/problems/image-overlap/

"""
Two images A and B are given, represented as binary, square matrices of the same size.  
(A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), 
and place it on top of the other image.  After, the overlap of this translation is the number of 
positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
"""

import collections

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        if not A or not A[0]:   return 0
        if not B or not B[0]:   return 0
        
        co1 = [(i, j) for i in range(len(A)) for j in range(len(A[0])) if A[i][j]]
        
        co2 = [(i, j) for i in range(len(B)) for j in range(len(B[0])) if B[i][j]]
        
        dist = collections.Counter((i - k, j - l) for i, j in co1 for k, l in co2)
        return max(list(dist.values()) + [0]) 