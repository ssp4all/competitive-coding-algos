https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums: return 0
        d = {}
        for i, val in enumerate(nums):
            if  val in d and i - d[val] <= k:
                return 1
            d[val] = i
        return 0