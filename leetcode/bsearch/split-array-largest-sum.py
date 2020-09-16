https://leetcode.com/problems/split-array-largest-sum/

"""
Given an array which consists of non-negative integers and an integer m, 
you can split the array into m non-empty continuous subarrays. Write an algorithm to 
minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if not nums:    return 0
        
        def helper(limit):
            tot = 0
            parts = 1
            for n in nums:
                tot += n
                if tot > limit:
                    parts += 1
                    tot = n
                    if parts > m:
                        return 0
            return 1
        maxi, sum_ = 0, 0
        for n in nums:
            sum_ += n
            maxi = max(maxi, n)
        l, r = maxi, sum_
        while l < r:
            mm = l + (r - l) // 2            
            if helper(mm):
                r = mm
            else:
                l = mm + 1
        return l
                