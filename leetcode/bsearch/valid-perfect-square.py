https://leetcode.com/problems/valid-perfect-square/

from math import sqrt

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if not num: return 0
        # x = int(sqrt(num))
        # return x ** 2 == num
        
        # i = 1
        # while num > 0:
        #     num -= i
        #     i += 2
        # return num == 0
        
        l, r = 0, num
        while l < r:
            m = l + (r - l) // 2
            if num == m * m:
                return 1
            elif num > (m * m):
                l = m + 1
            else:
                r = m
        return (l * l) == num
            