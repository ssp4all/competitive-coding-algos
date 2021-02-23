https://leetcode.com/problems/arithmetic-slices/

"""
A sequence of numbers is called arithmetic if it consists 
of at least three elements and if the difference between 
any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7
"""

# TC:O(N), SC:O(N)
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A:   return 0 
        n = len(A)
        count = 0
        for i in range(n - 2):
            d = A[i + 1] - A[i]
            for j in range(i + 2, n):
                if d == A[j] - A[j - 1]:
                    count += 1
                else:
                    break 
        return count

# TC:O(N), SC:O(N) #recursive
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A:   return 0 
        n = len(A)
        total = 0
        
        def slices(index):
            nonlocal total
            if index < 2:  
                return 0 
            count = 0
            if A[index] - A[index - 1] == A[index - 1] - A[index - 2]:
                count = 1 + slices(index - 1)
                total += count
            else:
                slices(index - 1)
            return count
        slices(n - 1) 
        return total