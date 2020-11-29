# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s: return 0
        n = len(s)
        l = 0
        r = n - 1
        # for i in range(n//2 + 1):
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        print(s)