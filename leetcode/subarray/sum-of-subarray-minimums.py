https://leetcode.com/problems/sum-of-subarray-minimums/

"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

"""

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        if not A:   return 0
        MOD = 10**9 + 7
        stack = []
        ans = 0
        dot = 0
        for ind, val in enumerate(A):
            count = 1
            while stack and stack[-1][0] >= val:
                v, c = stack.pop()
                count += c
                dot -= v * c
            
            stack += [(val, count)]
            dot += (val 

                * count)
            ans += dot
        return ans % MOD


# very easy
"""
idea is to use stack and dp
for ex [3,1,2, 5, 4]
3  | [3]                                             -> 3
1  | [3, 1], [1]                                     -> 1, 1
2  | [3, 1, 2] [1, 2] [2]                            -> 1, 1, 2
5  | [3, 1, 2 ,5] [1, 2, 5] [2, 5] [5]               -> 1, 1, 2, 5
4  | [3, 1, 2, 5, 4] [1,2, 5, 4] [2, 5,4] [5, 4] [4] -> 1, 1, 2, 4, 4

i.,e res[i] = res[j] + A[i]*(i - j) where (j < i)  
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        if not arr: return 0
        arr = [0] + arr
        n = len(arr)
        res = [0] * n 
        stack = [0]
        for i, val in enumerate(arr):
            while arr[stack[-1]] > val:
                stack.pop()
            
            last_smallest = stack[-1]
            res[i] = res[last_smallest] + (i - last_smallest) * arr[i]
            stack += [i]
        return sum(res) % (10**9 + 7)