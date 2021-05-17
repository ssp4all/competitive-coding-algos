#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'nodeDistance' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts UNWEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#
import collections
def nodeDistance(g_nodes, g_from, g_to):
    # Write your code here
    # print(g_nodes, g_from, g_to)
    graph = collections.defaultdict(set)
    for a, b in zip(g_from, g_to):
        graph[a].add(b) 
        graph[b].add(a) 
    
    dist = [0] * (g_nodes + 1)
    # cycles = set()
    #find all node with cycles 
    
    
    def dfs(u, p):
        nonlocal cycleno
        if color[u] == 2:   return 
        if color[u] == 1:
            cycleno += 1
            cur = p 
            mark[cur] = cycleno 
            while cur != u:
                cur = par[cur]
                mark[cur] = cycleno 
            return 
        par[u] = p 
        color[u] = 1 
        for v in graph[u]:
            if v == par[u]:
                continue 
            dfs(v, u)
        color[u] = 2
            
    color = [0] * (g_nodes + 1)
    par = [0] * (g_nodes + 1)
    mark = [0] * (g_nodes + 1)
    cycles = collections.defaultdict(list)
    
    cycleno = 0
    dfs(1, 0)
    
    for i in range(1, g_nodes + 1):
        if mark[i] != 0:
            cycles[mark[i]] += [i]
    
    
    print(cycles)
    
    new = set()
    for a, b in cycles.items():
        for val in b:
            new.add(val)
    print(new)
    for i in range(1, g_nodes + 1):
        seen = set()
        if i in new: continue 
        # perform BFS 
        dq = collections.deque([(i, 0)])
        while dq:
            size = len(dq)
            tmp = collections.deque()
            for _ in range(size):
                nei, d = dq.popleft()
                seen.add(nei) 
                if nei in new:
                    dist[i] = d
                    break  
                for x in graph[nei]:
                    if x not in seen:
                        tmp += [(x, d + 1)]
            if dq:  break 
            dq = tmp  

    return dist[1:]
            
                

if __name__ == '__main__':




#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'smallestNegativeBalance' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY debts as parameter.
#
import collections
def smallestNegativeBalance(debts):
    # Write your code here
    if not debts:   return "Nobody has a negative balance"
    # print(debts)
    bank = collections.defaultdict(int)
    
    for a, b, c in debts:
        bank[a] -= int(c) 
        bank[b] += int(c) 
    
    mini = min(bank.items(), key=lambda x:x[1])
    if mini[1] >= 0:
        return ["Nobody has a negative balance"]
    ans = []
    for a, b in bank.items():
        if b == mini[1]:
            ans += [a]
    return sorted(ans)
if __name__ == '__main__':