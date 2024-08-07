https://leetcode.com/problems/evaluate-division/

"""
You are given equations in the format A / B = k, where A and B are variables 
represented as strings, and k is a real number (floating-point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will 
result in no division by zero and there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
"""

# BETTER 
# TC: O(Q * (E + V)) V = total variables, E = edges or Equations 
# SC: O(V) 

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)
        for eq, v in zip(equations, values):
            a, b = eq
            g[a][b] = v
            g[b][a] = 1 / v
        
        seen = set()
        def dfs(curr, tar, seen):
            seen.add(curr)
            if curr == tar: return 1
            for nei in g[curr]:
                if nei in seen:  continue 
                if nei == tar:  return g[curr][nei]
                tmp = dfs(nei, tar, seen)
                if tmp == -1:   
                    continue
                return tmp * g[curr][nei]
            return -1
        ans = []
        for que in queries:
            a, b = que
            seen.clear()
            if a not in g or b not in g:
                ans.append(-1)
                continue
            tmp = dfs(a, b, seen)
            ans.append(tmp)
        return ans

############################################################

# TC: O(Q*N)
from collections import defaultdict
from numpy import prod

class Solution:
    def calcEquation(self, equations: List[List[str]], vals: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set)
        values = defaultdict(float)
        
        output = []
        
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].add(b)
            values[(a, b)] = vals[i]
            graph[b].add(a)
            values[(b, a)] = 1 / vals[i]
        
        def dfs(char, tar, val, seen):
            if char in seen:    return -1.0
            seen.add(char)
            
            for child in graph[char]:
                if child == tar:
                    return prod(val) * values[(char, child)]
                x = dfs(child, tar, val + [values[(char, child)]], seen)
                if x != -1.0:
                    return x
            return -1.0
        
        for a, b in queries:
            seen = set()
            res = dfs(a, b, [], seen)
            output += [res]
        return output
"""
[["a","b"],["b","c"]]
[2.0,3.0]
[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
[["a","b"],["b","c"],["bc","cd"]]
[1.5,2.5,5.0]
[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
[["a","b"]]
[0.5]
[["a","b"],["b","a"],["a","c"],["x","y"]]
"""
            