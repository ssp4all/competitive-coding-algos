https://leetcode.com/problems/minimum-height-trees/

"""
For an undirected graph with tree characteristics, 
we can choose any node as the root. The result graph is then a rooted tree. 
Among all possible rooted trees, those with minimum height are called 
minimum height trees (MHTs). Given such a graph, write a function to 
find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. 
You will be given the number n and a list of undirected edges 
(each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] and 
thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not n or not edges:  return [0]
        
        adj = {i:set() for i in range(n)}
        op = {i:0 for i in range(n)}

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        seen = set()
        
        def dfs(node):
            if node in seen:
                return 0
            seen.add(node)
            x =  1 + max([dfs(i) for i in adj[node]])
            
            return x
    
        for i in range(n):
            seen.clear()
            op[i] = dfs(i)
        print(op)
        
        ans = [i for i, j in op.items() if j == min(op.values()) ]
        return ans


BFS
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not n or not edges:  return [0]
        
        adj = {i:set() for i in range(n)}
        op = {i:0 for i in range(n)}

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        seen = set()
        
        for i in range(n):
            dq = collections.deque([(i, 0)])
            seen.clear()
            while dq:
                n, d = dq.popleft()
                if n in seen:
                    continue
                op[n] = max(op[n], d + 1)
                seen.add(n)
                for j in adj[n]:
                    dq.append((j, d + 1))
                    
        # print(op)
        ans = [i for i, j in op.items() if j == min(op.values()) ]
        return ans

Optimal
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not n or not edges:  return [0]
        
        adj = {i:set() for i in range(n)}

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        l = [i for i in range(n) if len(adj[i]) == 1]
        # print(adj, l)
        while n > 2:
            n -= len(l)
            nl = []
            for i in l:
                node = adj[i].pop()
                adj[node].remove(i)
                if len(adj[node]) == 1:
                        nl.append(node)
                l = nl
            return l