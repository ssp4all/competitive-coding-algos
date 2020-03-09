https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, no: int, pre: List[List[int]]) -> bool:
        if not pre: return 1
        
        g = {i:[] for i in range(no)}
        
        for i, j in pre:
            if i == j:  continue
            g[i].append(j)
        # print(g)  
        
        def dfs(c):
            if not g[c] or c in comp:
                comp.add(c)
                return 1
            else:
                if c in temp:
                    return 0
                temp.add(c)
                for i in g[c]:
                    x = dfs(i)
                    if not x:   return x
                comp.add(c)
                return 1
            
        comp = set()
        
        for i in range(no):
            temp = set()
            x = dfs(i)
            print(x)
            if x == 0: return x
        return 1 if len(comp) == no else 0

#Find order
class Solution:
    def findOrder(self, no: int, pre: List[List[int]]) -> List[int]:
        if not pre or not pre[0]: return [i for i in range(no)]
        
        g = {i:[] for i in range(no)}
        
        for i, j in pre:
            if i == j:  continue
            g[i].append(j)
        # print(g)  
        
        def dfs(c):
            if not g[c]: 
                if c not in comp:
                    comp.append(c)
                return 1
            elif c in comp:
                return 1
            else:
                if c in temp:
                    return 0
                temp.add(c)
                for i in g[c]:
                    x = dfs(i)
                    if not x:   return x
                if c not in comp:
                    comp.append(c)
                return 1
            
        comp = []
        
        for i in range(no):
            temp = set()
            x = dfs(i)
            # print(x)
            if x == 0: return []
        # print(comp)
        return comp if len(comp) == no else []


"""
BFS
"""
from collections import defaultdict, deque

class Solution:
    def findOrder(self, no: int, pre: List[List[int]]) -> List[int]:
        if not pre or not pre[0]: return [i for i in range(no)]
        
        g = {i:set() for i in range(no)}
        neigh = defaultdict(set)
        
        for i, j in pre:
            g[i].add(j)
            neigh[j].add(i)
        
        res = []
        que = deque([i for i in g if not g[i]])
        while que:
            node = que.popleft()
            res.append(node)
            for i in neigh[node]:
                g[i].remove(node)
                if not g[i]:
                    que.append(i)
        # print(res)
        return res if len(res) == no else []
        

Indegree


class Solution:
    def canFinish(self, no: int, pre: List[List[int]]) -> bool:
        if not pre:
            return 1

        indegree = {i: 0 for i in range(no)}

        g = defaultdict(set)
        for i, j in pre:
            g[i].add(j)
            indegree[j] += 1

        que = deque(
            list(filter(lambda t: (indegree[t] == 0), indegree.keys())))
        # print(que, g, indegree)
        order = []
        if not que:
            return 0
        while que:
            v = que.popleft()
            for x in g[v]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    que.append(x)
            order.append(v)

        # print(order)
        return len(order) == no
