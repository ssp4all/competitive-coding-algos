# https://leetcode.com/problems/valid-palindrome/
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return 1
        # x = s.translate(str.maketrans(',', ' ', "!?';.:"))
        x = re.sub(r'\W', '', s)
        print(x)
        x = "".join(x.lower().split())
        s = x
        # print(s, x[::-1])
        return s == x[::-1]