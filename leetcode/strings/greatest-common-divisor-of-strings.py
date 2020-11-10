# https://leetcode.com/problems/greatest-common-divisor-of-strings

"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t  
(t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides 
both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
"""

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
