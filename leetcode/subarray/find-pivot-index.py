https://leetcode.com/problems/find-pivot-index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums: return -1
        n = len(nums)
        left, right = [0]*n, [0]*n
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, n):
            left[i] += (nums[i] + left[i-1])
        for i in range(n-2, -1, -1):
            right[i] += (nums[i] + right[i+1])
        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1


class Solution(object):
    def pivotIndex(self, nums):
        if not nums: return -1
        n = len(nums)
        sumR, sumL = sum(nums), 0
        for i in range(n):
            sumL += nums[i]
            if sumL == sumR:
                return i
            sumR -= nums[i]
        return -1

# class Solution(object):
#     def pivotIndex(self, nums):
#         S = sum(nums)
#         leftsum = 0
#         for i, x in enumerate(nums):
#             if leftsum == (S - leftsum - x):
#                 return i
#             leftsum += x
#         return -1