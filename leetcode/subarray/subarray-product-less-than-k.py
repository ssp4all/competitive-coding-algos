https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        if k <= 1: return 0
        n = len(nums)
        prod = 1
        left = 0
        ans = 0
        for i, val in enumerate(nums):
            prod *= val
            while left < n and prod >= k:
                prod /= nums[left]
                left += 1
            ans += (i-left+1)
        return ans