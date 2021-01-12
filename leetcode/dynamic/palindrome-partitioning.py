https://leetcode.com/problems/palindrome-partitioning/

"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""

# TC: O(N*N*2^N)
# SC: O(N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:   return []
        
        def check(ss):
            size = len(ss)
            i = 0
            while i <= size // 2:
                if ss[i] != ss[~i]:
                    return 0 
                i += 1
            return 1
        res = []
        
        def helper(s, path):
            nonlocal res
            if not s:
                res += [path]
                return
            for i in range(1, len(s) + 1):
                if check(s[:i]):
                    helper(s[i:], path + [s[:i]])
            return
        helper(s, [])
        return res