https://leetcode.com/problems/advantage-shuffle/

"""

Given two arrays A and B of equal size, the advantage 
of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

Example 1:
Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
"""

# TC:O(NlgN), SC:O(N)
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        A.sort() 
        
        heap = [] #should be a max-heap
        for i in range(n):
            b = B[i]
            heappush(heap, (-b, i))
            
        slow, fast = 0, n - 1
        ans = [0] * n
        while heap:
            val, idx = heappop(heap)
            if -val >= A[fast]:
                ans[idx] = A[slow]  
                slow += 1
            else:
                ans[idx] = A[fast]  
                fast -= 1
        
        return ans