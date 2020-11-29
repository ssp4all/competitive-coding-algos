https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

"""
Given a string s and an integer k, return the length of the 
longest substring of s such that the frequency of each character
 in this substring is greater than or equal to k.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times 
and 'b' is repeated 3 times.
"""

class Solution:
    @functools.lru_cache(None)
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or k > len(s):   return 0
        less_freq = min(set(s), key=s.count)
        if s.count(less_freq) >= k:  return len(s)
        return max(self.longestSubstring(item, k) for item in s.split(less_freq))