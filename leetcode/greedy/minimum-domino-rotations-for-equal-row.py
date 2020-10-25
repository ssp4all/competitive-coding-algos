https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, 
as indicated by the second figure.
"""
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        countA, countB, countAB = [0] * 7, [0] * 7, [0] * 7
        
        for i in range(n):
            countA[A[i]] += 1
            countB[B[i]] += 1
            if A[i] == B[i]:
                countAB[A[i]] += 1

        for i in range(1, 7):
            if countA[i] + countB[i] - countAB[i] == n:
                return n - max(countA[i], countB[i])
        return -1
        
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        def get_rotation(A, B, num):
            rotation = 0
            for i in range(len(A)):
                if A[i] == num: continue
                if B[i] != num: return float('inf')
                rotation += 1
            return rotation
        
        
        mini = float('inf')
        for i in range(1, 7):
            mini = min(mini, get_rotation(A, B, i))
            mini = min(mini, get_rotation(B, A, i))
        
        return mini if mini != float('inf') else -1

"""
[2,1,2,4,2,2]
[5,2,6,2,3,2]
[1,2,3,4,6]
[6,6,6,6,5]
"""