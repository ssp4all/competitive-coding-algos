https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        n = len(a)
        if n < 3: return 0
        i = 0
        while i+1 < n and a[i] < a[i+1]:
            i += 1
        
        if not i or i == n-1:
            return 0
        while i+1 < n and a[i] > a[i+1]:
            i += 1
        return i == n-1