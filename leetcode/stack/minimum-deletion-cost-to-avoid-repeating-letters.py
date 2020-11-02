https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/

"""
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, 
after deleting a character, the costs of deleting other characters will not change.

 

Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical 
letters next to each other).
"""

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if not s:   return 0
        tot = 0
        stack = []
        for index, val in enumerate(s):
            if stack and stack[-1][0] == val:
                if stack[-1][1] < cost[index]:
                    ch, c = stack.pop()
                    tot += c
                else:
                    tot += cost[index]
                    continue
            stack += [(val, cost[index])]
        
        return tot

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if not s:   return 0
        tot = 0
        max_cost = 0
        for i in range(n):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            tot += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])
        return tot