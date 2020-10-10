https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        prod = 1
        ans = -9**9
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                ans = max(ans, prod)
        return ans

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        r = imax = imin = nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(nums[i], nums[i]*imax)
            imin = min(nums[i], nums[i]*imin)

            r = max(r, imax)

        return r

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        r = imax = imin = nums[0]
        for i in range(1, n)
            prev = imax
            imax = max(nums[i], nums[i]*imax, nums[i]*imin)
            imin = min(nums[i], nums[i]*imin, nums[i]*prev)
            # print(imin)
            r = max(r, imax)

        return r