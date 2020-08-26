https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0: break
            if i> 0 and nums[i] == nums[i-1]: continue
            
            l, r = i+1, n-1
            while l < r:
                tot = nums[l] + nums[r] + nums[i]
                
                if tot > 0:
                    r -= 1
                elif tot < 0:
                    l += 1
                else:
                    ans.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
        return ans
                    