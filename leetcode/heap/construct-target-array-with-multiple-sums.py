https://leetcode.com/problems/construct-target-array-with-multiple-sums


"""
Given an array of integers target. From a starting array, 
A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size 
and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target
 array from A otherwise return False.

 

Example 1:

Input: target = [9,3,5]
Output: true
"""

class Solution:
    def isPossible(self, target):
        heap = []
        for num in target: heappush(heap, -num)
        s = sum(target)
        while True:
            elem = -heappop(heap)
            if elem == 1: return True
            if s == elem: return False
            cand = elem - (s - elem)
            if cand == elem or cand < 1: return False
            s = s - elem + cand
            heappush(heap, -cand)



#upsolving 
O(nlogn) to build up the priority queue.

class Solution:
    def isPossible(self, target):
        heap = []
        for num in target: heappush(heap, -num)
        s = sum(target)
        while True:
            elem = -heappop(heap)
            if elem == 1: return True
            if s == elem: return False
            cand = (elem - 1) % (s - elem) + 1
            if cand == elem: return False
            s = s - elem + cand
            heappush(heap, -cand)