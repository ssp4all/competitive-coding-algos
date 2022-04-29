# https://leetcode.com/problems/redundant-connection/

# n this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n,
#  with one additional edge added. The added edge has two different vertices chosen 
#  from 1 to n, and was not an edge that already existed. The graph is represented 
#  as an array edges of length n where edges[i] = [ai, bi] indicates that there is an
#  edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
# If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

        
# TC:O(V*E)
# SC:O(V+E)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(source, tar): #
            if source in seen:  return 0 
            seen.add(source)
            if source == tar:   return 1 
            return any(dfs(nei, tar) for nei in graph[source])
        
        
        graph = defaultdict(set)
        # idea is to for a new edge keep on checking if node in the current can reach 
        # to the another node in the same edge
        for i, j in edges:
            seen = set()
            if i in graph and j in graph and \
                dfs(i, j):
                return [i, j]
            graph[i].add(j)
            graph[j].add(i)

# Optmization 
# This can be solved using DSU algorithm in O(V*$V) = O(V) TC 