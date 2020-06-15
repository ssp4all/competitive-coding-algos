https://leetcode.com/problems/possible-bipartition/

"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 
"""
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(set)
        for u, v in dislikes:
            graph[u].add(v)
            graph[v].add(u)

        color = dict()
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node)
                   for node in range(1, N+1)
                   if node not in color)