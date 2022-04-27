# https://leetcode.com/problems/smallest-string-with-swaps/submissions/


# You are given a string s, and an array of pairs of indices in 
# the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

# You can swap the characters at any pair of indices in the given pairs any number of times.

# Return the lexicographically smallest string that s can be changed to after using the swaps.

 

# Example 1:

# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"


class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            sx, sy = self.size[px], self.size[py]
            if sx > sy:
                self.parent[py] = px
                self.size[px] += sy
            else:
                self.parent[px] = py
                self.size[py] += sx

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        N = len(s)
        dsu = DSU(N)
        g = defaultdict(list)
        for a, b in pairs:
            g[a].append(b)
            g[b].append(a)
            
        for a, b in g.items():
            for item in b:
                dsu.union(a, item)
        
        #components
        comp = defaultdict(list)
        for i in range(N):
            comp[dsu.find(i)].append(s[i])
        
        for v in comp.values():
            v.sort(reverse=True)
            
        res = []
        for i in range(N):
            res.append(comp[dsu.find(i)].pop())
        return ''.join(res)
            