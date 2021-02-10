https://leetcode.com/problems/connecting-cities-with-minimum-cost/

"""
There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents 
the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting 
city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections 
(possibly of length 1) that connects those two cities together.  The cost is the sum of the 
connection costs used. If the task is impossible, return -1.


Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.

"""
TC:O(ElgV), SC:O(V)
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        
        edges  = defaultdict(list)
        
        for st, end, cost in connections:
            edges[st] += [(cost, end)]
            edges[end] += [(cost, st)]
        start = connections[0][0]
        
        tot= 0
        heap = [(0, start)]

        seen = set()
        while heap and len(seen) < N:
            cost, nei = heappop(heap)
            if nei in seen: continue
            seen.add(nei)
            tot += cost
        
            for cost, n in edges[nei]:
                heappush(heap, (cost, n))
        if len(seen) < N:
            return -1
        return tot