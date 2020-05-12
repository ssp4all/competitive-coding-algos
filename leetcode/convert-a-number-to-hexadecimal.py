https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution:
    def toHex(self, num: int) -> str:
        
        m = "0123456789abcdef"
        ans = ""
        while num != 0:
            # print(num, ans)
            n = num & 15
            ans = m[n] + ans
            num >>= 4
            if len(ans) > 7:    break
        return ans.lstrip('0') if ans else "0"
            