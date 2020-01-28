https://leetcode.com/problems/longest-increasing-subsequence/

Brute  force

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
		def helper(prev, cur):
		    if cur == n:    return 0
		    taken = 0
		    if nums[cur] > prev:
		        taken = 1 + helper(nums[cur], cur+1)

		    nottaken = helper(prev, cur+1)
		    return max(taken, nottaken)

		return helper(float('-inf'), 0)

Memoization

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)        
        memo = [[-1]*n for _ in range(n)]
        def helper(previ, cur):
            if cur == n:    return 0
            if memo[previ+1][cur] >= 0:
                return memo[previ + 1][cur]
            taken = 0
            if previ < 0 or nums[cur] > nums[previ]:
                taken = 1 + helper(cur, cur + 1)
            nottaken = helper(previ, cur + 1)
            memo[previ + 1][cur] = max(taken, nottaken)
            return memo[previ + 1][cur]        
        return helper(-1, 0)

DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = 1
        ans = 1
        for i in range(1, n):
            mv = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    mv = max(mv, dp[j])
            dp[i] = mv + 1
            ans = max(ans, dp[i])
        return ans
        
Find the number of longest-increasing-subsequence
eg., 12435->(1,2,4,5) and (1,2,3,5)

class Solution:
    def findNumberOfLIS(self, nums):
        dp = [[1, 1] for i in range(len(nums))]
        max_for_all = 1
        for i, num in enumerate(nums):
            max_len, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    if dp[j][0] + 1 > max_len:
                        max_len = dp[j][0] + 1
                        count = 0 
                    if dp[j][0] == max_len - 1:
                        count += dp[j][1]
            dp[i] = [max_len, max(count, dp[i][1])]
            max_for_all = max(max_len, max_for_all)
        print(dp, max_for_all)
        return sum([item[1] for item in dp if item[0] == max_for_all])
