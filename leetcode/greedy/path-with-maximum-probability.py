https://leetcode.com/problems/path-with-maximum-probability/


"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by 
an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b 
with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success 
to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it 
differs from the correct answer by at most 1e-5.

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2

Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2
 and the other has 0.5 * 0.5 = 0.25.
"""
# TC:O(V*V), SC:O(V*V)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        #idea is to use backtracking 
        """
        psuedocode
        - maitain seen array 
        - func cur -> cur-val 
            cur = 0 to stoer max val 
            for nei in neighs:
                cur = max(cur, func(nei))
            return cur-prob * func()
        """
        #build a graph 
        graph = defaultdict(set)
        unique = defaultdict(float)
        
        for index, (a, b) in enumerate(edges):
            graph[a].add(b)
            graph[b].add(a)
            unique[(a, b)] = succProb[index]
            unique[(b, a)] = succProb[index]
            
        seen = set()
        visited = set()
        def backtrack(cur, prev, seen):
            
            seen.add(cur)
            visited.add(cur)
            cur_edge = unique[(cur, prev)] if prev != -1 else 1
            if cur == end:
                seen.remove(cur)
                return cur_edge
            maxi = float('-inf')
            for nei in graph[cur]:
                if nei not in seen:
                    maxi = max(maxi, backtrack(nei, cur, seen))
            seen.remove(cur)
            return maxi * cur_edge if maxi != float('-inf') else cur_edge
        
        prob = backtrack(start, -1, seen) 
        if end not in visited:
            return 0.00000
        return prob if prob != 1 else 0.00000


 ###########################################
 # Upsolving 
 # TC:O(ElgV), SC:O(V)
 class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        #idea is to use Dijkstra 
        #build a graph 
        graph = defaultdict(set)
        prob_mapping = defaultdict(float)
        
        for index, (a, b) in enumerate(edges):
            graph[a].add(b)
            graph[b].add(a)
            prob_mapping[(a, b)] = succProb[index]
            prob_mapping[(b, a)] = succProb[index]
       
        #start dijkstra
        heap = [(-1, start)]
        seen = set() 
        
        while heap:
            cur_prob, node = heappop(heap)
            if node == end:
                return -cur_prob 
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    heappush(heap, (cur_prob*prob_mapping[(node, nei)], nei))
        return 0.00000