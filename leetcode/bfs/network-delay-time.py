https://leetcode.com/problems/network-delay-time/

"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), 
where u is the source node, v is the target node, and w is the time it takes 
for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes 
to receive the signal? If it is impossible, return -1.

"""
from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mat = [[float('inf') ] * n for _ in range(n) ] 
        for i, j, w in times:
            mat[i - 1][j - 1] = w
        k -= 1
        seen = set()
        ans = 0
        q = [(0, k)]
        while q:
            t, node = heappop(q)
            if node in seen :
                continue
            ans = max(ans, t)
            seen.add(node)
            for ind, v in enumerate(mat[node]):
                if v == float('inf') or ind in seen:   
                    continue
                heappush(q, (t+v, ind))
        if len(seen) == n:
            return ans
        else:
            return -1

from heapq import *
from collections import*
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for i, j, w in times:
            g[i] += [(j, w)]

        seen = set()
        pq = []
        for i, w in g[k]:
            heappush(pq, (w, i))
        time = 0
        seen = {k}
        while pq:
            c, node = heappop(pq)
            # print(c, node)
            if node in seen:    continue
            seen.add(node)
            time = max(time, c)
            for child, w in g[node]:
                heappush(pq, (w + c, child))
            
        if len(seen) == n:
            return time
        return -1