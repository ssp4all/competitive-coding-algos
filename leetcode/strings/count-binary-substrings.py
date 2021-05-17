https://leetcode.com/problems/count-binary-substrings/


"""
Give a string s, count the number of non-empty 
(contiguous) substrings that have the same number of 
0's and 1's, and all the 0's and all the 1's in these 
substrings are grouped consecutively.

Substrings that occur multiple times are counted 
the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:   return 0 
        count = 0
        groups = itertools.groupby(s)
        seq = [len(list(v)) for k, v in groups]
        n = len(seq)
        for i in range(n - 1):
            count += min(seq[i], seq[i + 1])
        return count