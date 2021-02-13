https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

"""
Given a string s, return the maximum number of ocurrences of any 
substring under the following rules:

The number of unique characters in the substring must be less than 
or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.
 
Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
"""

# TC: O(N*K) K = minSize
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        count = Counter([s[i: i + minSize] for i in range(len(s) - minSize + 1)])
        return max([val for k, val in count.items() if len(set(k)) <= maxLetters], default=0)
