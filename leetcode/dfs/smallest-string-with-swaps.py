https://leetcode.com/problems/smallest-string-with-swaps/

"""
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
"""

from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        graph = defaultdict(set)
        
        for a, b in pairs:
            graph[a].add(b)
            graph[b].add(a)
        
        seen = set()
        ans = list(s)
        n = len(s)
        def dfs(i, comp, seen):
            seen.add(i)
            comp += [i]
            for j in graph[i]:
                if j not in seen:
                    dfs(j, comp, seen)
        
        for i in range(n):
            if i in seen:   continue
            component = []
            dfs(i, component, seen)
            component.sort()
            chars = sorted([ans[c] for c in component])
            
            for i in range(len(component)):
                ans[component[i]] = chars[i]
                
        return "".join(ans)
#####################################################
class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.count = n
        
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px==py:
            return
        self.count-=1
        if self.rank[px]>self.rank[py]:
            self.parent[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px]=py
            self.rank[py]+=self.rank[x]
        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        dsu = DSU(n)
         # [[0,3],[1,2],[0,2]]
        for x,y in pairs:
            dsu.union(x,y)
        # [0,1,2,3]
        
        # Club everyone with the same parent
        if dsu.count == 1:
            return "".join(sorted(s))
        hm = collections.defaultdict(list)
        for i in range(n):
            hm[dsu.find(i)].append(s[i])
        for key in hm:
            hm[key].sort(reverse=True)
        res = []
        for i in range(n):
            res.append(hm[dsu.find(i)].pop())
        return "".join(res)
            
        