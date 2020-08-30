https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        n = len(nums)
        for i in range(n):
            ind = abs(nums[i]) - 1
            if nums[ind] > 0:
                nums[ind] *= -1
        op =[]
        for j in range(1, n+1):
            if nums[j-1] > 0:
                op.append(j)
        return op

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        x = set(range(1, len(nums)+1)) - (set(nums))
        return (x)