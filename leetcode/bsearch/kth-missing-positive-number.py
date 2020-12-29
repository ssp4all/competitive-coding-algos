https://leetcode.com/problems/kth-missing-positive-number/

"""
Given an array arr of positive integers sorted in a strictly increasing order, 
and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing
 positive integer is 6.
"""

# O(lgN)
class Solution:
    def findKthPositive(self, A, k):
        l, r = 0, len(A)
        while l < r:
            m = (l + r) // 2
            if A[m] - 1 - m < k: #logic is (A[m] - 1 + 1) - (m + 1)
                l = m + 1
            else:
                r = m
        return l + k

########################################
# O(N)
        arr = [0] + arr
        n = len(arr)
        
        prev = 0
        
        for i in range(1, n):
            diff = arr[i] - prev - 1
            if k - diff <= 0:
                break
            k -= diff 
            prev = arr[i]
        
        return prev + k