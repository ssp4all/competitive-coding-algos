https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:    return 0
        n = len(nums)
        summ, ans = 0, -1
        j = 0
        dict = {}
        for i in range(n):
            summ += nums[i]
            if summ == k:
                ans = max(ans, i + 1)
            if summ - k in dict:
                ans = max(ans, i - dict[summ - k])
            dict[summ] = i
        return ans if ans != -1 else 0
            