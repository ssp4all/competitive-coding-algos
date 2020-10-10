https://leetcode.com/problems/maximum-length-of-pair-chain


"""Greedy"""
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
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs: return pairs
        pairs.sort()
        n = len(pairs)
        dp = [1]*n
        for j in range(n):
            for i in range(j):
                # print(j, i)
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i]+1)
                    # break
                    # print(dp)
        return max(dp)