https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

"""
Given an array of integers nums and an integer threshold, we will choose a 
positive integer divisor and divide all the array by it and sum the result of the division. 
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. 
(For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 
the sum will be 5 (1+1+1+2). 
"""

import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if not nums:    return 0
        n = len(nums)
        
        left, right = 1, max(nums) + 1
        ans = float('inf')
        def check(div):
            sum_ = 0
            for num in nums:
                sum_ += math.ceil(num / div)
                if sum_ > threshold:
                    return -1
            return sum_
        
        while left < right:
            m = left + (right - left) // 2
            if check(m) > 0:
                ans = min(ans, m)
                right = m 
            else:
                left = m + 1
        return ans
                
        