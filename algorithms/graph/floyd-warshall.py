# Floyd Warshall Algo(All pair shortest path)
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance 

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for a, b, w in edges:
            dist[a][b] = dist[b][a] = w
        for i in range(n):
            dist[i][i] = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
