https://leetcode.com/problems/minimum-moves-to-equal-array-elements

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if not nums:    return -1
        n = len(nums)
        j = 0

        while True:
            mini = maxi = nums[0]
            mi = mx = 0
            for i in range(1, n):
                if nums[i] > maxi:
                    maxi = nums[i]
                    mx = i
                elif nums[i] < mini:
                    mini = nums[i]
                    mi = i
                    
            if nums[mi] - nums[mx] == 0:
                return j
            for i in range(n):
                j += abs(nums[i] - mx)
        return j
        
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if not nums:    return -1
        n = len(nums)
        j = 0
        nums.sort()
        ans  = 0
        for i in range(n - 1, 0, -1):
            xx = nums[i] - nums[0]
            ans += xx
        return ans

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if not nums:    return -1
        return sum(nums) - (len(nums) * min(nums))