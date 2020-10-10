# https://leetcode.com/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(2, n):
            nums[i] = max(nums[i-2] + nums[i], nums[i-1])
        return nums[n-1]

# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:    return 0
        n = len(nums)
        l, r = [0]*(n - 1), [0]*(n)
        if n == 1:  return nums[0]
        elif n == 2:  return max(nums[0], nums[1])
        # elif n == 3:    return nums[1]
        l[0], r[1] = nums[0], nums[1]
        l[1] = max(nums[0], nums[1])
        r[2] = max(nums[1], nums[2])
        for i in range(2, n - 1):
            l[i] = max(l[i - 1], nums[i] + l[i - 2])
        # print(l)
        for i in range(3, n):
            r[i] = max(r[i - 1], nums[i] + r[i - 2])
        # print(r)
        return max(l[-1], r[-1])