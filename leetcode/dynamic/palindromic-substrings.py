https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:   return 0
        n = len(s)
        ans = []
        l, r = 0, 0
        for c in range(2 * n - 1):
            l = c // 2
            r = l + c % 2
            
            while l >= 0 and r < n and s[l] == s[r]:
                ans.append(s[l:r + 1])
                l -= 1
                r += 1
        # print(ans)
        return len(ans)