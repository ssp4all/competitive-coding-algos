https://leetcode.com/problems/find-k-closest-elements/

"""
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. 
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        diff = []
        for num in arr:
            diff += [(abs(num - x), num)]
        diff.sort()
        return sorted([val for diff, val in diff[:k]])

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n - k
        
        while left < right:
            m = left + (right - left) // 2
            if x - arr[m] > arr[m + k] - x:
                left = m + 1
            else:
                right = m
        return arr[left: left + k]