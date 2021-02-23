https://leetcode.com/problems/number-of-operations-to-make-network-connected/

"""
There are n computers numbered from 0 to n-1 connected by ethernet cables 
connections forming a network where connections[i] = [a, b] represents a 
connection between computers a and b. Any computer can reach any other 
computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain 
cables between two directly connected computers, and place them between 
any pair of disconnected computers to make them directly connected. 
Return the minimum number of times you need to do this in order to
 make all the computers connected. If it's not possible, return -1. 

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
"""

class Solution:
    def makeConnected(self, n: int, conn: List[List[int]]) -> int:
        if len(conn) < n - 1:   return -1
        visited = [0] * n
        adj = {i:set() for i in range(n) }
        for i, j in conn:
            adj[i].add(j)
            adj[j].add(i)
        ans = 0
        
        def dfs(i):
            visited[i] = 1
            for j in adj[i]:
                if not visited[j]:
                    dfs(j)
        
        for i in adj:
            if not visited[i]:
                dfs(i)
                ans += 1
        return ans - 1