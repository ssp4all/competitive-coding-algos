https://leetcode.com/problems/broken-calculator/

class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        ans = 0
        if x == y:  return ans
        elif x > y: return x - y
        
        while y > x:
            ans += 1
            if y % 2 == 1:
                y += 1
            else:
                y //= 2
        return ans + (x - y)