import heapq
import collections

# prims's algorithm
def solve(N, connections):
    if not connections: return []

    pq = []
    ans = []
    edges = collections.defaultdict(list)

    for t1, t2, cost in connections:
        edges[t1].append((t2, cost))
        edges[t2].append((t1, cost))

    seen = set()
    random_start = connections[0][0]
    seen.add(random_start)

    for outgoing_edge, cost in edges[random_start]:     
        heapq.heappush(pq, (cost, random_start, outgoing_edge))

    while pq and len(seen) < N:
        cost, t1, t2 = heapq.heappop(pq)
    
        if t1 in seen and t2 in seen: 
            continue
        ans += [[t1, t2, cost]]
        if t1 not in seen:
            for outgoing_edge, cost in edges[t1]: 
                heapq.heappush(pq, (cost, t1, outgoing_edge))
            seen.add(t1)
        if t2 not in seen:
            for outgoing_edge, cost in edges[t2]: 
                heapq.heappush(pq, (cost, t2, outgoing_edge))
            seen.add(t2)

    if len(seen) < N: 
        return []
    print(edges, seen)
    # print(ans)
    return ans
connections = [["A", "B", 1], ["B", "C", 4], ["B", "D", 6], ["D", "E", 5], ["C", "E", 1]]
x = solve(5, connections)
print(x) 