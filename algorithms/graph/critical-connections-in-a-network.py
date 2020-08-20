https://leetcode.com/problems/critical-connections-in-a-network/

"""
Solves both articulation and critical connections
"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        g = [[] for _ in range(n)]
        
        for i, j in connections:
            g[i] += [j]
            g[j] += [i]
        
        time = 0
        p = [-1] * n
        vis = [0] * n
        disc = [float('inf')] * n
        low = [float('inf')] * n
        # ap = [0] * n
        ans = []

        def dfs(u):
            nonlocal time, ans
            # child = 0
            vis[u] = 1

            disc[u] = time
            low[u] = time
            time += 1
            for v in g[u]:
                if vis[v] == 0:
                    # child += 1
                    p[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    # if p[u] == -1 and child > 1:
                    #     ap[u] = 1
                    # if p[u] != -1 and low[v] >= disc[u]:
                    #     ap[u] = 1
                    if low[v] == disc[v]:
                        ans += [[u, v]]
                else:
                    if v != p[u]:
                        low[u] = min(low[u], disc[v])
        for i in range(n):
            dfs(i)
        # print(ans)
        return ans