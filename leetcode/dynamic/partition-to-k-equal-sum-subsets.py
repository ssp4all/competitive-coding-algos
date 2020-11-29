https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

"""
Given an array of integers nums and a positive integer k, find whether it's possible
 to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""
#Time Complexity as per the editorial is O(k^(n - k) * k!)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or not k:   return 0
        tar, rem = divmod(sum(nums) , k)
        if rem:     return 0
        nums.sort()
        
        def helper(grps):
            if not nums:    return 1
            x = nums.pop()
            for i, grp in enumerate(grps):
                if grp + x <= tar:
                    grps[i] += x
                    if helper(grps):    return 1
                    grps[i] -= x
                if not grp:    break
            nums.append(x)
            return 0
        
        if nums[-1] > tar:  return 0
        while nums and nums[-1] == tar and k:
            # print(nums)
            nums.pop()
            k -= 1
        # print(nums)
        return helper([0] * k)

For two subsets

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:    return 0
        k = 2
        tar, rem = divmod(sum(nums), k)
        if rem:     return 0
        nums.sort()
        
        def helper():
            if not nums: return 1
            x = nums.pop()
            for i, val in enumerate(arr):
                if val + x <= tar:
                    arr[i] += x
                    if helper():    return 1
                    arr[i] -= x
                if not val: break
            nums.append(x)
            return 0
                
        
        while nums and nums[-1] == tar and k:
            nums.pop()
            k -= 1
        
        arr = [0] * k
        return helper()

##########################################
# Time Complexity: O(2^n * k)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:    return 0 
        
        sum_, maxi = 0, float('-inf')
        n = len(nums)
        
        for num in nums:
            sum_ += num
            maxi = max(maxi, num)
        
        # print(maxi, sum_)
        if maxi > (sum_ // k) or (sum_ % k) != 0:   return 0
        
        target = sum_ // k
        
        #end edge cases check
        
        used = [0] * n
        
        def helper(cur, start, k):
            if k == 0:  return 1

            if cur == target:   
                return helper(0, 0, k - 1)

            for i in range(start, n):
                if not used[i] and cur + nums[i] <= target:
                    used[i] = 1
                    if helper(cur + nums[i], i + 1, k):
                        return 1
                    used[i] = 0
            return 0
        print('test')
        return helper(0, 0, k)
