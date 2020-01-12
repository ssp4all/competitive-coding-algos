https://leetcode.com/problems/shortest-unsorted-continuous-subarray


"""O(n*lgn)"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        xx = sorted(nums)
        s, e = n, 0
        for i in range(n):
            if nums[i] != xx[i]:
                s = min(s, i)
                e = max(e, i)
        return (e-s+1) if e-s > 0 else 0

"""O(n)"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        stack = []
        s, e = n, 0
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                ind = stack.pop()
                s = min(s, ind)
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                
                ind = stack.pop()
                e = max(e, ind)
            stack.append(i)   
            # print(stack)
        return e-s+1 if e-s > 0 else 0