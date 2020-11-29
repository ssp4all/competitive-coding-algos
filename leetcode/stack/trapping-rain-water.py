https://leetcode.com/problems/trapping-rain-water/

"""
Given n non-negative integers representing an elevation map where 
the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of 
rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9 
"""

Brute force
class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:  return 0
        
        n = len(heights)
        
        water = 0
        for i in range(n):
            left = 0
            right = 0
            j = i
            while j >= 0:
                left = max(left, heights[j])
                j -= 1
            k = i
            while k < n:
                right = max(right, heights[k])
                k += 1
            water += min(left, right) - heights[i]
        return water

Optimal
class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:  return 0
        
        n = len(heights)
        
        l, r = 0, n - 1
        max_left, max_right = 0, 0
        water = 0
        while l < r:
            if heights[l] < heights[r]:
                if heights[l] > max_left:
                    max_left = heights[l]
                else:
                    water += max_left - heights[l]    
                l += 1
            else:
                if heights[r] > max_right:
                    max_right = heights[r]
                else:
                    water += max_right - heights[r]
                r -= 1
        return water