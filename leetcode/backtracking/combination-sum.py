https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, nums: List[int], tar: int) -> List[List[int]]:
        if not nums:    return []
        n = len(nums)
        ans = set()
        def bt(temp, remain, st):
            if remain < 0:
                return
            elif remain == 0:
                ans.add(tuple(temp))
            else:
                for i in range(st, n):
                    bt(temp + [nums[i]], remain - nums[i], i)
                    
        bt([], tar, 0)
        return ans