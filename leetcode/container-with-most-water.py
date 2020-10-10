https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        l, r = 0, n-1
        ans = 0
        while l < r:
            ans = max(ans, (r-l)*min(height[r], height[l]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans