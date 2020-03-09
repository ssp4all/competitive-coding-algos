https://leetcode.com/problems/minimum-size-subarray-sum


""" Brute force"""
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        ans, sum =float('inf'), 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if sum >= s:
                    ans = min(ans, j-i+1)
                    break
        return ans if ans != float('inf') else 0


""" Two pointer O(n) """
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        ans, sum, left = float('inf'), 0, 0
        for i in range(n):
            sum += nums[i]
            while sum >= s:
                ans = min(ans, i-left+1)
                sum -= nums[left]
                left += 1

        return ans if ans != float('inf') else 0


"""For maximum subarray length with sum K"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        n = len(nums)
        d = {}
        ans = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            if sum - k in d:
                ans = max(ans, i - d[sum-k])
            d[sum] = i
        return ans
