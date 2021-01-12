https://leetcode.com/problems/4sum/


# TC: O(n^(k - 1))


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:    return []
        results = set()
        n = len(nums)
        
        def helper(l, r, target, N, cur):
            if r - l + 1 < N or N < 2 or nums[l] * N > target or target > nums[r] * N:
                return 
            
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.add(tuple(cur + [nums[l], nums[r]]))
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
                
            else:
                for i in range(l, r + 1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        helper(i + 1, r, target - nums[i], N - 1, cur + [nums[i]])
        nums.sort()
        helper(0, n - 1, target, 4, [])
        return results