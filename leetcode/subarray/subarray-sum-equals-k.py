https://leetcode.com/problems/subarray-sum-equals-k/

"""Brute force"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        n = len(nums)
        # sum = [0]*(n+1)
        # for i in range(1, n+1):
        #     sum[i] = sum[i-1] + nums[i-1] 
        ans = 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                # ss = sum[j] - sum[i]
                if sum == k:
                    ans += 1
        return ans

"""O(n) """
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        n = len(nums)
        d = {0:1}
        count = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            if sum - k in d:
                count += d[sum-k]
            d[sum] = d.get(sum, 0) + 1
        return count
