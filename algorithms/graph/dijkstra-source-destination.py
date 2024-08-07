from collections import *
from heapq import *

#TC: O(ElgV) where E = edges and V = Vertices
# SC: O(V + E)
conn = [["A", "B", 4], ["B", "C", 10], ["A", "C", 41]]
def dijkstra(conn, src, dest):
    g = defaultdict(list)
    for c in conn:
        st, end, cost = c
        g[st] += [(cost, end)]
        g[end] += [(cost, st)]
    print(g)
    heap, seen, dist = [(0, src, ())], set(), {src: 0}
    while heap:
        cost, node, path = heappop(heap)
        if node in seen:    continue
        path = (node, path)
        seen.add(node)
        if node == dest:
            return [cost, path]
        for w, ch in g.get(node, []):
            # if ch in seen:  continue
            new_dist = cost + w
            old_dist = dist.get(ch, None)
            if old_dist is None or  old_dist > new_dist:
                dist[ch] = new_dist
                heappush(heap, (new_dist, ch, path))
    return float('inf')


x = dijkstra(conn, "A", "C")
print(x)


##############################################
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = defaultdict(list)
        for a, b, w in edges:
            g[a].append([b, w])
            g[b].append([a, w])

        def dfs(i):
            heap = [(0, i)]
            dist = {i: 0}          
            while heap:
                curr, node = heapq.heappop(heap)
                for nei, w in g[node]:
                    new_d = curr + w
                    if new_d < dist.get(nei, float('inf')): 
                        dist[nei] = new_d
                        heapq.heappush(heap, (new_d, nei))     