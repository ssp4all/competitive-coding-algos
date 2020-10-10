https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        if not arr: return 0
        memo = {}
        ans = float('-inf')
        for num in arr:
            memo[num] = memo.get(num-diff, 0) + 1
            ans = max(ans, memo[num])
        return ans