https://leetcode.com/problems/largest-rectangle-in-histogram/

"""
Given n non-negative integers representing the histogram's bar height 
where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        area = -1
        stack = []
        ind = 0
        for ind, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                val = stack.pop()
                if stack:
                    area = max(area, heights[val] * (ind - stack[-1] - 1))
                else:
                    area = max(area, heights[val] * ind)
                    
            stack += [ind]
                               
        ind += 1
        while stack:
            val = stack.pop()
            if stack:
                area = max(area, heights[val] * (ind - stack[-1] - 1))
            else:
                area = max(area, heights[val] * ind)
        return area