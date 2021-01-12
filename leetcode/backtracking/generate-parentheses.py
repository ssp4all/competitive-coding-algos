https://leetcode.com/problems/generate-parentheses/

"""
Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
# Brute force 
# TC: O(n*2^2n), SC:O(n*2^2n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n: return []
        ans = []
        
        def isvalid(a):
            if not a: return 0
            bal = 0
            tt = list(a)
            for t in tt:
                if t == "(":
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return 0
            return bal == 0
        
        def backtrack(a, n):
            if n < 0:   return 
            if n == 0 and isvalid(a) == 1:
                ans.append(a)
            else:
                for b in s:
                    backtrack(a+b, n-1)
        s = ['(', ')']
        backtrack("", 2*n)
        return ans


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(a = []):
            print(a)
            if len(a) == 2*n:
                if isvalid(a):
                    ans.append("".join(a))
            else:
                a.append("(")
                generate(a)
                a.pop()
                a.append(')')
                generate(a)
                a.pop()
        def isvalid(a):
            bal = 0
            for c in a:
                if c == "(":
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return 0
            return bal == 0
            
        ans = []
        generate()
        return ans

# Optimal
# O(2^n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(a="", l=0, r=0):
            if len(a) == 2*n:
                ans.append(a)
            if l < n:
                backtrack(a+"(", l+1, r)
            if r < l:
                backtrack(a+")", l, r+1)
            
        ans = []
        backtrack()
        return ans