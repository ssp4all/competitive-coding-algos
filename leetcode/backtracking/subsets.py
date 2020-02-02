https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        n = len(nums)
        ans = set()
        
        def bt(temp, st):
            if tuple(temp) not in ans:
                ans.add(tuple(temp))
            for i in range(st, n):
                bt(temp + [nums[i]], i+1)
        bt([], 0)      
        return ans
                    

https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        # nums = list(set(nums))
        nums.sort()
        n = len(nums)
        ans = set()
        
        def bt(temp, st):
            if tuple(temp) not in ans:
                ans.add(tuple(temp))
            for i in range(st, n):
                # if nums[i] in temp: continue
                bt(temp + [nums[i]], i+1)
        bt([], 0)      
        return ans
                    