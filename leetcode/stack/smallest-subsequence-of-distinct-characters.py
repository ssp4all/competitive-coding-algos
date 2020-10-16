https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

"""
Return the lexicographically smallest subsequence of s that contains all the distinct 
characters of s exactly once. 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:   return s
        last = {ch: ind for ind, ch in enumerate(s)}
        
        stack = []
        for ind, ch in enumerate(s):
            if ch in stack: continue
            while stack and ch < stack[-1] and ind < last[stack[-1]]:
                stack.pop()
            stack += [ch]
        return "".join(stack)
            