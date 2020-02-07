https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        
        n = len(nums)
        ans = set()
        
        def BT(temp, no):
            if no == 0:
                ans.add(tuple(temp))
            else:
                for i in nums:
                    if i in temp:   continue
                    BT(temp + [i], no-1)
        BT([], n)
        return ans

from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        return permutations(nums)


With duplicates

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:    return nums
        ans = set()
        n = len(nums)
        
        def bt(temp, no, used):
            if no == 0:
                ans.add(tuple(temp))
                return
            else:
                for i in range(n):
                    if used[i]: continue
                    used[i] = 1
                    bt(temp + [nums[i]], no - 1, used)
                    used[i] = 0
        used = [0]*n
        bt([], n, used)
        return ans

Next permutations

https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums
        n = len(nums)
        left = n - 2
        
        def reverse(ptr):
            r = n - 1
            while ptr < r:
                nums[ptr], nums[r] = \
                    nums[r], nums[ptr]
                r -= 1
                ptr += 1
        
        while left > -1:
            if nums[left] < nums[left + 1]:
                right = left + 1
                while right < n and nums[left] < nums[right]:
                    right += 1
                right -= 1
                nums[left], nums[right] = \
                    nums[right], nums[left]
                reverse(left + 1)
                return 
            left -= 1
        reverse(0)
        return 
            