https://leetcode.com/problems/is-graph-bipartite/

"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into 
two independent subsets A and B such that every edge in the graph has one 
node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j 
for which the edge between nodes i and j exists.  Each node is an integer 
between 0 and graph.length - 1.  There are no self edges or parallel edges: 
graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
"""
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph = {i:set() for i in range(1, N + 1)}
        for i, j in dislikes:
            graph[i].add(j)
            graph[j].add(i)
        color = dict()

        def helper(node, cur):
            if node in color:
                return color[node] == cur
            color[node] = cur
            for n in graph[node]:
                if not helper(n, cur ^ 1):
                    return 0
            return 1
        
        for i in range(1, N + 1):
            if i not in color:
                if not helper(i, 0):
                    return 0
        return 1