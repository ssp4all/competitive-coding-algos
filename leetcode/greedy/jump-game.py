https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return -1
        n = len(nums)
        
        def helper(cur):
            if cur >= n - 1:
                return 1
        
            for i in range(1, nums[cur] + 1):
                if helper(cur + i):
                    return 1
        
            return 0
        return helper(0)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:    return 0
        n = len(nums)
        if n <= 1 and nums[0] == 0: return 1
        if nums[0]  == 0:   return 0
        
        cur = nums[0]
        maxi = cur
        for i in range(1, n):
            if i + nums[i] > maxi:
                maxi = i + nums[i]
                if maxi >= n - 1:
                    return 1
                
            if cur == i:
                cur = maxi
            if i >= cur and i != n - 1:
                return 0
            
        if maxi >= n - 1:
            return 1
        else:
            return 0