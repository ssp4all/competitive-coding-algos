https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return -1
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        print(heap)
        heapq.heapify(heap)
        print(heap)
        
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                print((matrix[i][j+1], i, j+1))
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret
        
class Solution(object):
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo+hi)//2
            x=0
            for row in matrix:
                print(x)
                x +=  bisect.bisect_right(row, mid) 
            # x = sum()
            print()

            if x < k:
                lo = mid+1
            else:
                hi = mid
        return lo