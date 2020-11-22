https://leetcode.com/problems/missing-element-in-sorted-array/

"""
Given a sorted array A of unique numbers, find the K-th missing 
number starting from the leftmost number of the array.


Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
"""

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums:    return 1
        prev = nums[0]
        
        for num in nums[1:]:
            diff = num - prev - 1
            if k - diff <= 0:
                break
            k -= diff
            prev = num
        return prev + k


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums:    return 1

        n = len(nums)
        
        diff = nums[-1] - nums[0] + 1
        missing = diff - n
        
        if missing < k:
            return nums[-1] + (k - missing)
            
        lo, hi = 0, n - 1
        while lo + 1 < hi:
            m = lo + (hi - lo) // 2
            missing = nums[m] - nums[lo] - (m - lo)
            if missing < k:
                lo = m
                k -= missing
            else:
                hi = m
            
        return nums[lo] + k