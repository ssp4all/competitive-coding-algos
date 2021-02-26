https://leetcode.com/problems/score-of-parentheses/

"""
Given a balanced parentheses string S, compute the score of the string 
based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
"""

# TC:O(N), SC:O(N)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        """
            ip = "(())" , "()()"
            s = [2]
        """
        
        stack = [0]         
        n = len(S)
        
        for i in range(n):
            cur = S[i]
            if cur == "(":
                stack += [0]
            else:
                val = stack.pop()
                stack[-1] += max(2 * val, 1)
        return stack.pop()
                    