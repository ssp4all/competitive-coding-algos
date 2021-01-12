https://leetcode.com/problems/maximal-square


class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        if not mat or not mat[0]:   return 0
        r, c = len(mat), len(mat[0])
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        
        ans = 0
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if mat[i - 1][j - 1] == "1":
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                    ans = max(ans, dp[i][j])
        # print(dp)   
        return ans ** 2