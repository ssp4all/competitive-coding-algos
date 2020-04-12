https://leetcode.com/problems/edit-distance/

"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2: return 0
        l1, l2 = len(word1), len(word2)
        
        dp = [[0] * (l1+1) for _ in range(l2+1)]
        # print(dp)
        dp[0][0] = 0
        
        for i in range(1, l1 + 1):
            dp[0][i] = i
        
        for i in range(1, l2 + 1):
            dp[i][0] = i
        # print(dp)
        
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            
                    
                    
        return dp[-1][-1]
        