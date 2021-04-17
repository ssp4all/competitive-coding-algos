https://leetcode.com/problems/redundant-connection/

"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes 
(with distinct values 1, 2, ..., N), with one additional edge added. 
The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element 
of edges is a pair [u, v] with u < v, that represents an undirected 
edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a 
tree of N nodes. If there are multiple answers, return the answer 
that occurs last in the given 2D-array. The answer edge [u, v] 
should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
"""

# TC:O(N^2), SC:O(N)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(source, tar):
            if source in seen:  return 0 
            seen.add(source)
            if source == tar:   return 1 
            return any(dfs(nei, tar) for nei in graph[source])
        
        
        graph = defaultdict(set)
        for i, j in edges:
            seen = set()
            if i in graph and j in graph and \
                dfs(i, j):
                return [i, j]
            graph[i].add(j)
            graph[j].add(i)

# NOTE: this is very easy using Union find template. 
# Idea is to join two nodes but if their parent is same then that's the answer
        
      