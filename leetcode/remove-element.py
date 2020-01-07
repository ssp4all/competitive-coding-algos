https://leetcode.com/problems/remove-element

class Solution(object):
    def removeElement(self, nums, val):
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
            

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        count = 0
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == val:
                del nums[l]
                r -= 1
            else:
                l += 1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        
        i, j, n = 0, 0, len(nums)
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                j += 1
                i += 1
            else:
                j += 1
        return (i)

""" 
remove-duplicates-from-sorted-array
leetcode.com/problems/remove-duplicates-from-sorted-array
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # return len(set(nums))
        l, n = 0, len(nums)
        r = n-1
        
        while l < r:
            if nums[l] == nums[l+1]:
                del nums[l]
                r -= 1
            else:
                l += 1
        return r+1