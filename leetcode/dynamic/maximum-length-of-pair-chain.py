https://leetcode.com/problems/maximum-length-of-pair-chain


"""Greedy"""

# TC:O(NlgN), SC:O(1)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs: return pairs
        pairs.sort(key=lambda x:x[1])
        ans = 0
        end = float('-inf')
        n = len(pairs)
        for i in range(n):
            if end < pairs[i][0]:
                end =  pairs[i][1]
                ans += 1
        return ans

"""Dynamic"""
# TC:O(NlgN + N^2), SC:O(1 + N)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs: return pairs
        pairs.sort()
        n = len(pairs)
        dp = [1]*n
        for j in range(n):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i]+1)
        return max(dp)

# Recursion with memo
# TC:O(NlgN + N), SC:O(1 + N)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort() 
        n = len(pairs)
        
        @functools.lru_cache(None)
        def helper(idx, prev):
            if idx >= n: return 0 
            
            st, end = pairs[idx]
            if st > prev:
                return max(1 + helper(idx + 1, end), helper(idx + 1, prev) )
            else:
                return helper(idx + 1, prev)
        
                           
        return helper(0, -1001)