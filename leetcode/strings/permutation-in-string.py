https://leetcode.com/problems/permutation-in-string/

"""
Given two strings s1 and s2, write a function to return true 
if s2 contains the permutation of s1. In other words, one of the 
first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:   return 1
        if not s1 or not s2:    return 0
        
        x = Counter(s1)
        ls1, ls2 = len(s1), len(s2)
        
        l, r = 0, 0
        y = Counter()
        while l < ls2 - ls1 + 1:
            while r < ls2 and r - l + 1 <= ls1:
                if s2[r] in x.keys():
                    y[s2[r]] += 1
                r += 1
            if x == y:
                return 1
            if s2[l] in x.keys():
                y[s2[l]] -= 1
            l += 1
        return 0

# OPtimized
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = collections.Counter(s1)
        
        count = len(need.keys())
        
        i = 0
        begin = 0
        while i < len(s2):
            if s2[i] in need:
                need[s2[i]] -= 1
                if need[s2[i]] == 0:
                    count -= 1
            i += 1
            while count == 0:
                if s2[begin] in need:
                    need[s2[begin]] += 1
                    if need[s2[begin]] > 0:
                        count += 1
                if i - begin == len(s1):
                    return 1
                begin += 1 
        return 0