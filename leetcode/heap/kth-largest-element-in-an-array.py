https://leetcode.com/problems/kth-largest-element-in-an-array/

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:    return -1
        n = len(nums)
        tar = n - k
        heap = nums[:k]
        heapify(heap)
        
        for i in range(k, n):
            heappushpop(heap, nums[i])
        return heappop(heap)

from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:    return -1
        heap = []
        for i in nums:
            heappush(heap, -i)
        for _ in range(k):
            x = heappop(heap)
        return x * -1

from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:    return -1
        heap = []
        for i in nums:
            if len(heap) < k:
                heappush(heap, i)
            else:
                heappushpop(heap, i)
        return heap[0]

class Solution:
    def findKthLargest(self, nums, k):
        if not nums:    return -1
        n = len(nums)
        
        def partition(l, r, pi):
            pivot = nums[pi]
            # nums[pi], nums[r] = nums[r], nums[pi]
            
            si = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[si], nums[i] = \
                            nums[i], nums[si]
                    si += 1
            nums[r], nums[si] = \
                    nums[si], nums[r]
            return si
            
        def select(l, r, tar):
            if l == r:
                return nums[l]
            pi = r #random works well 
            pi = partition(l, r, pi)
            if tar == pi:
                return nums[tar]
            elif tar < pi:
                return select(l, pi-1, tar)
            else:
                return select(pi+1, r, tar)
                
        return select(0, n-1, n-k)
        