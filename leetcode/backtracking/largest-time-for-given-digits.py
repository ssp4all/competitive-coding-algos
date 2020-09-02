https://leetcode.com/problems/largest-time-for-given-digits/

from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        li = list(permutations(A))
        # print(li)
        maxi = -1
        for i, j, k, l in li:
            hour = i * 10 + j
            minutes = k * 10 + l
            if hour < 24 and minutes < 60:
                maxi = max(maxi, hour * 60 + minutes) 
                
        return "{:02d}:{:02d}".format(maxi // 60, maxi % 60) if maxi != -1 else ""