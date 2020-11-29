https://leetcode.com/problems/kth-missing-positive-number/

# O(lgN)
class Solution:
    def findKthPositive(self, A, k):
        l, r = 0, len(A)
        while l < r:
            m = (l + r) // 2
            if A[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k

########################################
O(N)
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