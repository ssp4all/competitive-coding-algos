# https://leetcode.com/problems/greatest-common-divisor-of-strings
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 and not str2:
            return ""
        if not str1 or not str2:
            return ""
        n1 = len(str1)
        n2 = len(str2)
        gcdd = gcd(n1, n2)
        ss = str1[:gcdd]
        return ss if gcdd*str1.count(ss) == n1 \
            and gcdd*str2.count(ss) == n2 else ""
