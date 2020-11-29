from collections import *
from heapq import *

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
            if ch in seen:  continue
            new_dist = cost + w
            old_dist = dist.get(ch, None)
            if old_dist is None or  old_dist > new_dist:
                dist[ch] = new_dist
                heappush(heap, (new_dist, ch, path))
    return float('inf')


x = dijkstra(conn, "A", "C")
print(x)