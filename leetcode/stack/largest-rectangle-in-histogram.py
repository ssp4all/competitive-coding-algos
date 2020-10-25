https://leetcode.com/problems/largest-rectangle-in-histogram/

"""
Given n non-negative integers representing the histogram's bar height 
where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
"""

Bruteforce O(n^2)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        n = len(heights)
        area = -1
        for i in range(n):
            mini = float('inf')
            for j in range(i, n):
                mini = min(mini, heights[j])
                area = max(area, mini * (j - i + 1))
        return area

OPtimal O(n)
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